#include "../stm32/lcd.h"
#include "py/obj.h"

void lcd_init(void) {}

void lcd_print_str(const char *str) { (void)str; }

void lcd_print_strn(const char *str, unsigned int len) {
  (void)str;
  (void)len;
}
