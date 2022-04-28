// str1 = "Welcome \tto my Blog"
// str2 = "Welcome to\n my \tBlog"
// console.log(str1)                
// console.log(str2)

// str="hello"
// console.log(str.slice(0,3))

// str="My Blog"
// a=""
// for (i of str){
//     a+=i
// console.log(a)
// }

// s='My'                        
// s1='Blog'                        
// s2=s.slice(0,2)+(s1).length-1                       
// print(s2)

               
// console.log("My"+"Blog" * 2)

// st="asdfghjkler"
// console.log(st[13])

// Q 33 (wrong)
// str1 = "Welcome to My Blog"
// for (i=0; i<=str1.length; i++){
//   s=""
//   for (j of str1){
//     // console.log(j)
//      if (j==" "){
//       //  console.log(" ")  
//      }
//      else{
//         s+=j  
//      }
// console.log(s)
//     }
// }

// str1="My position is 1st and my friend come on 4th"

// TITLE FUNCTION
// name="my name is sakshi"
// n=name.split(" ")
// for (i in n){
// for (j in n[i]){
// if (j==0){
// console.log(n[i][j].toUpperCase())
// }
// if (j!=0){
// console.log(n[i][j].toLowerCase())
// }
// }
// }

// console.log(typeof(Infinity))

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// let text = fruits.constructor;
// console.log(text)

// const fruits =["Banana", "Orange","kiwi", "Apple", "Mango", "Papaya","grapes","pineapple"];
// fruits.copyWithin(3, 1,4);
// console.log(fruits)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// const f = fruits.entries();
// for (let x of f) {
// console.log(x)
// }

// const ages = [32, 33, 89, 40];
// ages.every(checkAge)
// function checkAge(ages) {
//   return ages > 18;
// }
// console.log(checkAge())

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.fill("Kiwi",2,3);
// console.log(fruits)

// const ages = [32, 33, 96, 40];
// const result = ages.filter(checkAdult);

// function checkAdult(age) {
//   return age >= 18;
// }
// console.log(checkAdult())

// name=require("readline-sync")
// name1=name.questionInt("enter number")
// name2=String(name1)
// name3=name2.split(" ")
// s=""
// for (i of name3){
// for (j in i){
// if (j==0){
//   s+="0"
// }
// else{
// s+=i[j]
// }
// }
// console.log(s)
// }

// i=0
// str=""
// do{
//    i++
//    j=5
//    do{
//       j--
//       str+=" "  
//    }while(j>=i)
//    k=0
//    do{
//       k++
//       str+="*"
//    }while(k<i)
//    str+="\n"
// }while(i<5)
// console.log(str)