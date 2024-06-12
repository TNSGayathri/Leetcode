class Solution:
    def reformatDate(self, date: str) -> str:
        d={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
        dat=date.split(" ")
        dat=dat[::-1]
        s=""
        for i in dat[-1]:
            if i.isdigit():
                s+=i
        if(len(s)!=2):
            s="0"+s
        return dat[0]+"-"+d[dat[1]]+"-"+s
                
        