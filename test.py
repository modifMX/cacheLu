# -*- coding:utf-8 -*-
EleObj={};
EleObj['整型']="1111"
EleObjquote=EleObj
print EleObj,'  ' ,EleObjquote;
EleObjquote['整型']=22222222
print EleObj,'  ' ,EleObjquote;
EleObj['整型']=1112
print EleObj,'  ' ,EleObjquote;
#修改值
#添加value
EleObj['integer']=[1,2,3];
print EleObj,'  ' ,EleObjquote;
#这些操作并没有什么鸟用
newObj={'a1':1,'b1':2,'c1':[1,2,3]}
print newObj
newCopyObj=newObj;
newCopyObj['c1'].remove(1)
print newObj," ",newCopyObj
################