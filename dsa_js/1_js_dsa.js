// primitive data types in JS
//numbers
const age =30
const pi=3.14
console.log(pi)
// string
const name="Alma x"
const message="Hello world"


// boolean 

const isTrue=true 
const isFalse=false

// null 

const person=null

//Undefined variables

let variaableWithoutvalues


// Symbol-Immutables

const id=Symbol("unique_id")

// non-primitive data types

// array
console.log("Primitive data types started")
let numbers=[1,24,5,43,5]
console.log(numbers[1])
console.log(numbers.length)

// Object

const person1= {
    name:"Rahul Raj",
    age:30,
    email:"rahul@almabetter.com",
    address:{
        city:"Delhi",
        country:"India"

    }
}
console.log(person1.name)
console.log(person1.address.country)

// Map 


let map=new Map()

map.set("id1","value1")
map.set("id2","value2")
console.log(map.get("id1"))



// set 

const uniqueNumbers=new Set([1,2,3,4,5,1])
console.log(uniqueNumbers)

// O(n) complexity
const array=[1,4,1,50,100,90]

function findMaxArray(array){
    let max=array[0] //1  4 50 100
    for ( let i=0;i<array.length;i++){
        if(array[i]>max){
            max=array[i];
        }
    }
    return max;

}
console.log("max value",findMaxArray(array))




