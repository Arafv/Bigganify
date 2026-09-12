[app]

title = Bigganify
package.name = bigganify
package.domain = com.bigganify

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.permissions = INTERNET
android.accept_sdk_license = True
android.allow_backup = True


[buildozer]

log_level = 2
warn_on_root = 0
