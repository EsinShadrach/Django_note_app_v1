const x_like_delete_btn = document.querySelectorAll(".delete")
const responding_tag = document.querySelectorAll(".tag")
console.log(responding_tag);

for (let i = 0; i < x_like_delete_btn.length; i++) {
    const element = x_like_delete_btn[i];
    element.addEventListener("click", ()=>{
        responding_tag[i].remove()
    })
}