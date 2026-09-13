[app]

# Title & metadata
title = Bigganify
package.name = bigganify
package.domain = org.bigganify

# Source code settings
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests, bin, venv, .git, .github

# Version & requirements
version = 0.1
requirements = python3,kivy

# UI configuration
orientation = portrait
fullscreen = 0

# Android SDK / NDK parameters
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.skip_update = False

[buildozer]

log_level = 2
warn_on_root = 1
# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

#
# Buildozer section
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn, 2 = error)
warn_on_root = 1
