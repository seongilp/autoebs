ffmpeg -re -i "https://ebsonair.ebs.co.kr/fmradiofamilypc/familypc1m/chunklist.m3u8" -vn -acodec copy -t 1200 "/home/runner/MouseEnglish_$(date +%Y%m%d-%H%M).m4a"
