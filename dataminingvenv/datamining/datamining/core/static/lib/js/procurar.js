/*$(document).ready(function(){

	$("#ordernator option:selected").each(function(){
		var div_list = $(".card");

		div_list.sort(function(a, b){
			return $(a).attr("id") - $(b).attr("id")
		});
		$("#dad").html(div_list);
		console.log(div_list)
	});
});

//$.get('/procurar/' + op, function(resposta){
//			alert(resposta)
	//	});