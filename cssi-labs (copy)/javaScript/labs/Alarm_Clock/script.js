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

console.log("script is running...");
function Basic_Alarm(alarmMessage){
  return alarmMessage;
};
console.log(Basic_Alarm("My alarm!"));

function My_Alarm(time){
  return "Hey,Esther, wake up! It is "+time;
};
console.log(My_Alarm("7:oo"));


function Mom_Alarm(time){
  return "Hey,Mom, wake up! It is "+time;
};
console.log(Mom_Alarm("5:oo"));

function Family_Alarm(time,Mom){
  return "Hey,Mom, wake up! It is "+time;
};
console.log(Family_Alarm("6:oo"));


function Important_Alarm(message){
  return message.toUpperCase();
};
console.log(Important_Alarm("wake up,wake up, wake up!!"));


function Snooze_Alarm(time){
  return "The alarm for " +time+" has been changed to "+ (time+1);
};
console.log(Snooze_Alarm(6));
