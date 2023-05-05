const color_hd = document.querySelector('#red_header');
const plain_hd = document.querySelector('header');
color_hd.onclick = () => {
    plain_hd.style.color = '#FF0000';
};
