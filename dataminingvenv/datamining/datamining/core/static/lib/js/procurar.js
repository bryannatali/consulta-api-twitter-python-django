$(document).ready(function(){

	$("#ordernator option:selected").each(function(){
		var ord = $(this).val();
		var div_list = $(".card");

		if (ord === "oldest"){
			div_list.sort(function(a, b){
			return $(a).attr("id") - $(b).attr("id")
			});
			$("#dad").html(div_list);
		} else if (ord === "newest") {
			div_list.sort(function(a, b){
			return $(b).attr("id") - $(a).attr("id")
			});
			$("#dad").html(div_list);
		}
		console.log(div_list)
	});
});

//$.get('/procurar/' + op, function(resposta){
//			alert(resposta)
	//	});