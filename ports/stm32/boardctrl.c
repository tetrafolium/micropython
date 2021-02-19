/*
 * This file is part of the MicroPython project, http://micropython.org/
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2013-2020 Damien P. George
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include "boardctrl.h"
#include "led.h"
#include "lib/utils/pyexec.h"
#include "py/mphal.h"
#include "usrsw.h"

STATIC void flash_error(int n) {
  for (int i = 0; i < n; i++) {
    led_state(PYB_LED_RED, 1);
    led_state(PYB_LED_GREEN, 0);
    mp_hal_delay_ms(250);
    led_state(PYB_LED_RED, 0);
    led_state(PYB_LED_GREEN, 1);
    mp_hal_delay_ms(250);
  }
  led_state(PYB_LED_GREEN, 0);
}

#if !MICROPY_HW_USES_BOOTLOADER
STATIC uint update_reset_mode(uint reset_mode) {
#if MICROPY_HW_HAS_SWITCH
  if (switch_get()) {

    // The original method used on the pyboard is appropriate if you have 2
    // or more LEDs.
#if defined(MICROPY_HW_LED2)
    for (uint i = 0; i < 3000; i++) {
      if (!switch_get()) {
        break;
      }
      mp_hal_delay_ms(20);
      if (i % 30 == 29) {
        if (++reset_mode > 3) {
          reset_mode = 1;
        }
        led_state(2, reset_mode & 1);
        led_state(3, reset_mode & 2);
        led_state(4, reset_mode & 4);
      }
    }
    // flash the selected reset mode
    for (uint i = 0; i < 6; i++) {
      led_state(2, 0);
      led_state(3, 0);
      led_state(4, 0);
      mp_hal_delay_ms(50);
      led_state(2, reset_mode & 1);
      led_state(3, reset_mode & 2);
      led_state(4, reset_mode & 4);
      mp_hal_delay_ms(50);
    }
    mp_hal_delay_ms(400);

#elif defined(MICROPY_HW_LED1)

    // For boards with only a single LED, we'll flash that LED the
    // appropriate number of times, with a pause between each one
    for (uint i = 0; i < 10; i++) {
      led_state(1, 0);
      for (uint j = 0; j < reset_mode; j++) {
        if (!switch_get()) {
          break;
        }
        led_state(1, 1);
        mp_hal_delay_ms(100);
        led_state(1, 0);
        mp_hal_delay_ms(200);
      }
      mp_hal_delay_ms(400);
      if (!switch_get()) {
        break;
      }
      if (++reset_mode > 3) {
        reset_mode = 1;
      }
    }
    // Flash the selected reset mode
    for (uint i = 0; i < 2; i++) {
      for (uint j = 0; j < reset_mode; j++) {
        led_state(1, 1);
        mp_hal_delay_ms(100);
        led_state(1, 0);
        mp_hal_delay_ms(200);
      }
      mp_hal_delay_ms(400);
    }
#else
#error Need a reset mode update method
#endif
  }
#endif
  return reset_mode;
}
#endif

void boardctrl_before_soft_reset_loop(boardctrl_state_t *state) {
#if !MICROPY_HW_USES_BOOTLOADER
  // Update the reset_mode via the default
  // method which uses the board switch/button and LEDs.
  state->reset_mode = update_reset_mode(1);
#endif
}

void boardctrl_top_soft_reset_loop(boardctrl_state_t *state) {
  // Turn on a single LED to indicate start up.
#if defined(MICROPY_HW_LED2)
  led_state(1, 0);
  led_state(2, 1);
#else
  led_state(1, 1);
  led_state(2, 0);
#endif
  led_state(3, 0);
  led_state(4, 0);
}

void boardctrl_before_boot_py(boardctrl_state_t *state) {
  state->run_boot_py = state->reset_mode == 1 || state->reset_mode == 3;
}

void boardctrl_after_boot_py(boardctrl_state_t *state) {
  if (state->run_boot_py && !state->last_ret) {
    flash_error(4);
  }

  // Turn boot-up LEDs off

#if !defined(MICROPY_HW_LED2)
  // If there is only one LED on the board then it's used to signal boot-up
  // and so we turn it off here.  Otherwise LED(1) is used to indicate dirty
  // flash cache and so we shouldn't change its state.
  led_state(1, 0);
#endif
  led_state(2, 0);
  led_state(3, 0);
  led_state(4, 0);
}

void boardctrl_before_main_py(boardctrl_state_t *state) {
  state->run_main_py = (state->reset_mode == 1 || state->reset_mode == 3) &&
                       pyexec_mode_kind == PYEXEC_MODE_FRIENDLY_REPL;
}

void boardctrl_after_main_py(boardctrl_state_t *state) {
  if (state->run_main_py && !state->last_ret) {
    flash_error(3);
  }
}

void boardctrl_start_soft_reset(boardctrl_state_t *state) {
  state->log_soft_reset = true;
}

void boardctrl_end_soft_reset(boardctrl_state_t *state) {
  // Set reset_mode to normal boot.
  state->reset_mode = 1;
}
