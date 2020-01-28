var list_name = ['玄关', '卫生间', '电视柜', '床头灯', '台灯'];
$("#btn_light").children().click(function () {
  btn = {
    'btn': this.value
  };
  console.log(btn);
  $.ajax({
    type: "post",
    url: "/apish/",
    dataType: "json",
    // contentType : "application/json",
    data: btn,
    success: function (d) {
      console.log(d);
    }
  });
});
$("#btn_tv").children().click(function () {
  btn = {
    'btn': this.value
  };
  console.log(btn);
  $.ajax({
    type: "post",
    url: "/apish/",
    dataType: "json",
    // contentType : "application/json",
    data: btn,
    success: function (d) {
      console.log('tv');
    }
  });
});
$("#btn_stb").children().click(function () {
  btn = {
    'btn': this.value
  };
  console.log(btn);
  $.ajax({
    type: "post",
    url: "192.168.1.109/apipk/",
    dataType: "json",
    // contentType : "application/json",
    data: btn,
    success: function (d) {
      console.log('stb');
    }
  });
});
