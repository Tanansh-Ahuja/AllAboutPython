import speedtest

print(speedtest)

test = speedtest.Speedtest()
down = test.download()
up = test.upload()
print("download: ",down);
print("upload: ",up)
