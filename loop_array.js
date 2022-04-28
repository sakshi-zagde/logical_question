// for (i=1; i<=10; i++){
// console.log(` ${i} = ${i*i}`)
// }

// i=100
// while (i>=10){
// console.log(i)
// i=i-10
// }

// ARRAY
// a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
// s=""
// for (i of a){
// for (j of i){
// s+=j
// }
// }
// console.log(s)

// list = [6,1,3,5,6,3,1]
// list1=[]
// pro=1
// for( i in list){
// for (j in list){
// if (! list1.includes(list[i])){
// list1.push(list[i])
// pro=pro*list1[i]
// }
// }
// }
// console.log(pro)

// name=require("readline-sync")
// name1=name.questionInt("enter number")
// name2=String(name1)
// s=""
// for (i in name2){
// len=name2.length-i
// s+=name2[i]+"0"*len
// console.log(s)
// s+="+"
// }

// l=[1, 1, 2, 3, 4, 4, 5, 1]
// // [[2, 1], 2, 3, [2, 4], 5, 1]
// s=[]
// for (i in l){
// f=[]
// count=0
// for (j in l){   
//      // console.log(i)
//      if (l[i]==l[j]){
//           count+=1
//           if (! f.includes(l[i])){
//           if (count==1){
//           } 
//           else{
//           f.push(l[i])
//           }
//           }
//      }
//      else{
//          if (! s.includes(l[i])){ 
//          s.push(l[i]) 
//          }
//      }     
// }
// f.push(count)
// if (! s.includes(f)){
// s.push(f)
// }
// }
// console.log(s)

// l=['Python', 'list', 'exercises', 'practice', 'solution']
// s=[]
// for (i in l){
// // for (j in i){
// move=l[i][Math.floor(Math.random()*l[i].length)]
// s.push(move)
// }
// // }
// console.log(s)

// array1=[]
// num=require("readline-sync")
// for (i=0; i<=3; i++){
// num1=num.questionInt("enter the num")
// array1.push(num1)
// }
// console.log(array1)

// for (i of array1){
// for (j of array1){
// for (k of array1){
// for (l of array1){
// if (i!=j && j!=k && i!=k && j!=l && l!=i && l!=k){
// console.log(j,i,k,l)
// }
// }
// }
// }}

// // op- ['12','68','43','95']
// l=[1,2,6,8,4,3,9,5]
// b=[]
// i=0
// while (i<len(l)-1){
//     j=i+1
//     k=String(l[i])+String(l[j])
//     b.push(k)
//     i=i+2
// }
// console.log(b) 

// // op- [[1,2],[6,8],[4,3],[9,5]]
// l=[1,2,6,8,4,3,9,5]
// b=[]
// i=0
// while (i<(l).length-1){
//     j=i+1
//     k=[(l[i]),(l[j])]
//     b.push(k)
//     i=i+2
// }
// console.log(b) 

// op- [[1,2],[2,6],[6,8],[8,4],[4,3],[3,9],[9,5]]
// l=[1,2,6,8,4,3,9,5]
// b=[]
// i=0
// while (i<(l).length-1){
//     j=i+1
//     k=[(l[i]),(l[j])]
//     b.push(k)
//     i=i+1
// }
// console.log(b) 

// l=[1, 3, 4, 5, 6, 7, 8, 9, 10]
// // Difference between elements (n+1th - nth) of the said list :
// // [1, 2, 1, 1, 1, 1, 1, 1]
// s=[]
// for (i=0; i<=(l.length)-2; i++){
// k=i+1
// d=l[k]-l[i]
// s.push(d)
// }
// console.log(s)

// l=[20,34,12,32,14,15,16]
// n=require("readline-sync")
// // n1=n.questionInt("enter which you want to remove")
// for(i in l){
// // n=require("readline-sync")
// i=n.questionInt("enter which you want to remove")
// l.splice(i)
// // console.log(l)
// }
// console.log(l)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruit = ["Banana", "Orange", "le", "ngo"];
// let text = fruits.join(fruit);
// console.log(text)

// const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
// const citrus = fruits.slice(1, 3);
// console.log(citrus)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.sort();
// fruits.reverse();
// console.log(fruits)

// const fruits = ["Banana", "Orange", "Apple", "Mango", "Kiwi"];
// fruits.splice(2, 2);
// console.log(fruits)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// let text = fruits.toString();
// console.log(text)

// SUM OF LIST
// l=[142, 67, 98, 34]
// s=[]
// for (i of l){
//      sum=0
//      for (j of String(i)){
//         sum=sum+(j%10)
//      }
//      s.push(sum)
// }
// console.log(s)

// d=['1', '2', '3', '4', '5', '6', '7', '8']
// // op-['12', '34', '56', '78']
// p=[]
// i=0
// while (i<d.length-1){
//      s=''
//      j=i+1
//      s+=d[i]
//      s+=d[j]
// p.push(s)
// i+=2
// }
// console.log(p)

// DIMENTIONS
// l=[[0, 1, 2], 
//    [2, 3, 4]]
// s=l.length
// for (i in l){
// d=l[i].length
// }
// console.log("metrix",s)
// console.log("dimention",d)

// l=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
// s=require("readline-sync")
// s1=s.question("enter. the element")
// for (i=0; i<l.length; i++){
//      if (s1===l[i]){
//      console.log(i)
//      }
// }



