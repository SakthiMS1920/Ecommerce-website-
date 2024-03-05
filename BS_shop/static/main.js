let button1 = document.querySelector(".lgo_bar"),/*here declaring log bar class (means navbar icon) as a button and that obj name is button1*/
    links1 = document.querySelector(".con2");/*here declaring content2 (con2) class (nav cintents with icon) as a links for the button(log bar)and that obj name is links1*/

  button1.addEventListener("click",() =>{   /*here caling the button1 obj as clicking butn*/
    links1.classList.toggle("display");  /*here caling the links1 obj as showing lik while clicking button1{with new object named diplay}this disply obj is uued to call links on css page*/
  
})
