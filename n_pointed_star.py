from turtle import*
n=21
outangle = 360/n
inangle = 180- outangle
noof_diag=n-2
angle =180-(inangle/noof_diag)


for i in range (n):
    right(angle);forward(200)

