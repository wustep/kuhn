$(function() {
	$("#tv-start").datepicker({ // Set up #date-start input element
	  defaultDate: "+1w",
	  changeMonth: true,
	  dateFormat: "yy-mm-dd",
	  numberOfMonths: 1
	});
	$("#tv-end").datepicker({ // Set up #date-end input element
	  defaultDate: "+1w",
	  changeMonth: true,
	  dateFormat: "yy-mm-dd",
	  numberOfMonths: 1
	});
	
	var nextMonday = moment().day(8);
	var nextFriday = moment(nextMonday).add(4, "days");
	$("#tv-start").attr('value', nextMonday.format('YYYY-MM-DD'));
	$("#tv-end").attr('value', nextFriday.format('YYYY-MM-DD'));
	
	$("#down").button().button("disable");
	$("#reset").button().button("disable");
	$("#gen").button().click(function() {
		$("#gen").button("disable");
		$("#down").button("enable");
		$("#reset").button("enable");
		$("#tv-start").datepicker("option", "disabled", "true");
		$("#tv-end").datepicker("option", "disabled", "true");
		
		var startDate = moment($("#tv-start").prop('value'));
		var endDate = moment($("#tv-end").prop('value'));
		var numDays = endDate.diff(startDate, "days") + 1;
		var curDate = startDate;
		for (var i = 1; i <= numDays; i++) {
			$("#output").append("<b><button type='submit' name='linkGet' value='"+i+"'>" + curDate.format("dddd") + "</button><b><br>");
			$("#output").append("<textarea id='date-"+i+"' name='date"+i+"' class='day-info-box'>"+curDate.format("MMMM D, YYYY")+"\r\nKuhn 100\r\n\r\nKuhn 102\r\n\r\nKuhn 200</textarea><br><br>");
			curDate = startDate.add(1, "days")
		}
	});
	$("#down").button().click(function() {
		$(".day-info-box").each(function() {
			var thisBox = this;
			$.post('tv.php', {tvNum: 1, date1: $(this).html()}, function(data) {
				$(thisBox).after(this);
			});
		});
	});
});