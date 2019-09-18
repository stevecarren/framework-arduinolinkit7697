# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http:", "", "www.apache.org", "licenses", "LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

"""

from os.path import isfile, isdir, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()

FRAMEWORK_DIR = platform.get_package_dir("framework-arduinolinkit7697")
assert isdir(FRAMEWORK_DIR)

variant_dir = join(FRAMEWORK_DIR, "variants", "linkit_7697")

env.Append(
    ASFLAGS=["-x", "assembler-with-cpp"],

    CFLAGS=[
        "-std=gnu99"
    ],

    CXXFLAGS=[
            "-std=c++11",
            "-c",
            "-mlittle-endian",
            "-mthumb",
            "-mcpu=cortex-m4",
            "-mfpu=fpv4-sp-d16",
            "-mfloat-abi=hard",
            "-gdwarf-2",
            "-Os",
            "-Wall",
            "-fno-rtti",
            "-fno-exceptions",
            "-ffunction-sections",
            "-fdata-sections",
            "-fno-builtin",
            "-fno-strict-aliasing",
            "-fno-common",
            "-DPCFG_OS=2",
            "-D_REENT_SMALL",
            "-MMD",
            "-Wno-literal-suffix"
    ],

    CCFLAGS=[
        "-c",
        "-mlittle-endian",
        "-mthumb",
        "-mcpu=cortex-m4",
        "-mfpu=fpv4-sp-d16",
        "-mfloat-abi=hard",
        "-gdwarf-2",
        "-Os",
        "-Wall",
        "-Wno-unused-parameter"
    ],

    CPPDEFINES=[
        ("PRODUCT_VERSION", "7697"),
        "MTK_BSPEXT_ENABLE",
        "USE_HAL_DRIVER",
        "MTK_NVDM_ENABLE",
        "MTK_DEBUG_LEVEL_INFO",
        "MTK_DEBUG_LEVEL_WARNING",
        "MTK_DEBUG_LEVEL_ERROR",
        "MTK_LWIP_ENABLE",
        "MTK_MINISUPP_ENABLE",
        "MTK_WIFI_API_TEST_CLI_ENABLE",
        "MTK_WIFI_REPEATER_ENABLE",
        "MTK_WIFI_WPS_ENABLE",
        ("MBEDTLS_CONFIG_FILE", '\\"config-mtk-websocket.h\\"'),
        "SUPPORT_MBEDTLS",
        "MTK_MINISUPP_ENABLE",
        "MTK_WIFI_TGN_VERIFY_ENABLE"
    ],

    CPPPATH=[
        join(FRAMEWORK_DIR, "cores", "arduino"),
        join(FRAMEWORK_DIR, "variants", "linkit_7697"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "driver", "chip", "mt7687", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "driver", "chip", "mt7687", "src", "common", "include"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "driver", "chip", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "driver", "CMSIS", "Device", "MTK", "mt7687", "Include"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "driver", "CMSIS", "Include"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "kernel", "rtos", "FreeRTOS", "Source", "include"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "kernel", "service", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "kernel", "rtos", "FreeRTOS", "Source", "portable", "GCC", "ARM_CM4F"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "third_party", "lwip", "src", "include"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "third_party", "lwip", "ports", "include"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "third_party", "mbedtls", "configs"), 
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "third_party", "mbedtls", "include"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "third_party", "httpclient", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "MTK", "connsys", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "MTK", "wifi_service", "combo", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "MTK", "bluetooth", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "prebuilt", "middleware", "MTK", "bluetooth", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "MTK", "nvdm", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "MTK", "dhcpd", "inc"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "src", "middleware", "MTK", "fota", "inc")
    ],

    LINKFLAGS=[
        "-mlittle-endian",
        "-mthumb",
        "-mcpu=cortex-m4",
        "-mfpu=fpv4-sp-d16",
        "-mfloat-abi=hard",
        "--specs=nano.specs",
        "-lnosys",
        "-nostartfiles",
        "-Wl,-wrap=malloc",
        "-Wl,-wrap=calloc",
        "-Wl,-wrap=realloc",
        "-Wl,-wrap=free",
        "-Wl,--check-sections",
        "-Wl,--gc-sections",
        "-Wl,-u",
        "-Wl,_printf_float",
    ],

    LIBS=[
        "c", 
        "m", 
        "gcc", 
        "stdc++",
        "liblinkit.a", 
        "libhal_core_CM4_GCC.a",
        "libnvdm_CM4_GCC.a", 
        "libhal_protected_CM4_GCC.a", 
        "libminicli.a", 
        "libwifi.a", 
        "libminisupp_wps.a", 
        "libble.a", 
        "libble_multi_adv.a", 
        "libbtdriver_7697.a"
    ],

    LIBPATH=[
        join(FRAMEWORK_DIR, "variants", "linkit_7697"),
        join(FRAMEWORK_DIR, "system", "linkit_7697", "libs")
    ]
)

env.ProcessFlags(board.get("build.framework_extra_flags.arduino", ""))

#
# Linker requires preprocessing with correct RAM|ROM sizes
#

if not isfile(join(variant_dir, "linkscripts", "mt7687_flash.ld")):
    print("Warning! Cannot find linker script for the current target!\n")

env.Replace(LDSCRIPT_PATH=join(variant_dir, "linkscripts", "mt7687_flash.ld"))

#
# Process configuration flags
#

cpp_defines = env.Flatten(env.get("CPPDEFINES", []))

# copy CCFLAGS to ASFLAGS (-x assembler-with-cpp mode)
env.Append(ASFLAGS=env.get("CCFLAGS", [])[:])

env.Append(
    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, "libraries", "__cores__", "arduino"),
        join(FRAMEWORK_DIR, "libraries")
    ]
)

#
# Target: Build Core Library
#

libs = []

env.BuildSources(
    join("$BUILD_DIR", "FrameworkArduinoVariant"),
    join(FRAMEWORK_DIR, "variants", "linkit_7697"))

env.BuildSources(
    join("$BUILD_DIR", "FrameworkArduino"),
    join(FRAMEWORK_DIR, "cores", "arduino"))

env.Prepend(LIBS=libs)
