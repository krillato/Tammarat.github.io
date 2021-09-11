# จับคู่คำทักทาย / บุคคล
'''
Hi,Hello
ไทม์,มิกซ์

็Hi ไทม์, Hi มิกซ์, Hello ไทม์, Hello มิกซ์

'''

greeting=['สวัสดี','Hi','Hello','Good Bye']
people=['ไทม์','มิกซ์','จี']
result=[]

#แบบปกติ
for x in greeting :
    for y in people :
        result.append(x+y)
print(result)

#แบบย่อ
result=[x+y for x in greeting for y in people]
print(result)