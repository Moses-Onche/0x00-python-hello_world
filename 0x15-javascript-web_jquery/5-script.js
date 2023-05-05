const item = '<li>Item</li>'
const list = 'UL.my_list'
$('DIV#add_item').click(function () {
  $(list).append(item);
});
