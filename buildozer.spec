[app]

title = Bigganify
package.name = bigganify
package.domain = org.bigganify
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf
version = 1.0
requirements = python3==3.11.8,kivy==2.3.0
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools = 34.0.0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
