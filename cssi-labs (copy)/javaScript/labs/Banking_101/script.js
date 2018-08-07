// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;

function openAccount(name,myBalance = 0){
  balance = myBalance;
  // Set the value for customer_name equal to name below
  customer_name =name;
  return name + " has opened a new account with a balance of $" + myBalance

  return //write the statment you need to return here


}

function deposit(value){
  balance = value
  return customer_name + "has deposited $"+ value +"." +customer_name + " total balance is $" +balance

  // update the value of balance
  //return the correct statement
}

function withdraw(amount){
  difference = balance - amount;
  if(difference < 0){
    return "sorry"+customer_name+ "you dont have amount in your account"

  }
  else{
    return customer_name + "has withdrawn" +amount+ "." +customer_name+ "has $" +balance+ "remaining"
  }
  //update the value of balance
  //return the correct statement
}

// Write your script below
console.log("script is running...");
