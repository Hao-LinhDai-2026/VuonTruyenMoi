[app]
title = Hon Truyen VIP
package.name = hontruyenvip
package.domain = org.haolinhdai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0.0

# Chứa đầy đủ thư viện thiết yếu cho hệ thống Text-to-Speech
requirements = python3,kivy,edge-tts,asyncio,aiohttp

orientation = portrait

# Cấp quyền internet bắt buộc để tải luồng âm thanh
android.permissions = INTERNET

# Tối ưu kiến trúc vi xử lý 64-bit mạnh nhất
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1

