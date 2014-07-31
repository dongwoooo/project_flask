$(document).ready(function(){
	$('#submit').click(function(){
		var keyword = $('#keyword').val();
		console.log(keyword);
		$.ajax({
			url:'/search',
			type:'POST',
			data:{"keyword":keyword},
			dataType:'json',
			success:function(response){
				console.log("received");
				$('.result').empty();
				for(var i = 0; i < response.length; i++){
					console.log(response[i].id);
					$('.result').append('<tr>' + '<td class="id">' + response[i].id + '</td>' + '<td class="mention">' + response[i].text + '</td>' + '</tr>');
				}
			},
			error:function(){
				console.log("error");
			},
			complete:function(){
				console.log("complete");
			}
		});
	});
});