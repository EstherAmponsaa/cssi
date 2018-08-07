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

console.log("Running Window Events Script");
window.addEventListener("keypress", e=> {
console.log(e.keyCode);
console.log(e.key);


})

let box6 = document.querySelector("#box6");
let size = 100;

window.addEventListener("keypress", e=> {
  if(e.key ==='c'){
    box6.style.borderRadius = "50%";
    box6.style.height = (size/2)+"px";
    box6.style.width = (size/2)+"px";
  }

  if(e.key ==='s'){
    box6.style.borderRadius = "0";
    box6.style.height = (size)+"px";
    box6.style.width = (size)+"px";
  }

});
let rect = document.querySelector("#rect");
window.addEventListener("scroll", e=> {
rect.style.backgroundColor = 'black';
});


// border-radius: 50%;
// insert a function that prints out the key code of a key pressed
