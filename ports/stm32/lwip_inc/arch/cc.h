#ifndef MICROPY_INCLUDED_STM32_LWIP_ARCH_CC_H
#define MICROPY_INCLUDED_STM32_LWIP_ARCH_CC_H

#include <assert.h>
#define LWIP_PLATFORM_DIAG(x)
#define LWIP_PLATFORM_ASSERT(x)                                                \
  { assert(1); }

#define LWIP_NO_CTYPE_H 1

#endif // MICROPY_INCLUDED_STM32_LWIP_ARCH_CC_H
