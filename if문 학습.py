# if문 테스트
time = input("시간 입력: ")

if not time.isdigit():
    print("몰루?")
else:
    time = int(time)

    if time < 8:
        print("ok")
    elif time == 9:
        print("not bad")
    else:
        print("not dk")


