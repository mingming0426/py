import random
print("========================歌王争霸赛===============================")
print("规则:输入隐藏字数，答对后评分")
user=input("挑战者姓名：")

songs=["少年","阳光开朗大男孩","我是未来","阳光彩虹小白马"]
lyrics=["我还是从前那个少年","阳光开朗大男孩","未来已来，我是未来","阳光彩虹小白马"]

score=0
for i in range(4):
    song=songs[i]
    lyric=lyrics[i]
    print("第"+str(i+1)+"首:"+song+",共"+str(len(lyric))+"个字")
    hidenum=input("请输入隐藏的字数:")
    lyriclist=list(lyric)

    count=0
    while True:
        idx=random.randint(0,len(lyriclist)-1)
        if lyriclist[idx]=="*":
            continue
        lyriclist[idx]="*"
        count+=1
        if count==int(hidenum):
            break
    lyric_show="".join(lyriclist)
    print(lyric_show)

    answer=input("请输入歌词:")
    if answer==lyric:
        score+=int(hidenum)
        print("当前得分："+str(score))
print("挑战结束，"+user+"的最终得分："+str(score))