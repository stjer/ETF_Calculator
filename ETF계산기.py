def tryint(justint=0):
    try : 
        a = input(" 입력 : \n")
        try:
            a=int(a)
        except:
            if justint==0:
                a=float(a)
            else:
                a = tryint(1)
        return a
    except: 
        print("숫자를 입력해 주세요.")
        a = tryint()
        return a

tst1 = []
tst2 = []

print("배율",end='')
tstr = tryint()#레버리지 배율

print("운용보수(%)",end='')
feerate = tryint()#운용보수
fee = 1-feerate/248#2023년 기준, 평일중 한국은 14, 미국은 12일 휴장 -> 247,249의 중간인 248일 휴장으로 임의로 계산.

#해당 부분은 단순 테스트용.
'''
tst = [100,90,100,110,100]
for i in range(1,10):
    tst2 = [100]
    tstr = i*0.1
    print('배율 : ',tstr)
    for _ in range(len(tst)-1):
        next0 = tst2[_]*((tst[_+1]/tst[_]-1)*tstr+1)*fee
        tst2.append(next0)
        print(next0)
    print()
'''
print("거래일수",end='')

lent = tryint(1)

for _ in range(lent):
    print(_+1,"번째 가격",end='')
    a = tryint()
    if a<0:
        lent=_
        break
    tst1.append(a)
    if _==0:
        tst2.append(a)
    if _==lent-1:
        print("/=======/")
    

for _ in range(lent-1):
        next0 = tst2[_]*((tst1[_+1]/tst1[_]-1)*tstr+1)*fee
        tst2.append(next0)
        print(next0)#이걸 주석처리하고 바깥에서 print(tst2)를 하는 방법도 있음.


