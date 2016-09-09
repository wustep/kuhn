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
			$("#output").append("<button type='submit' name='linkGet' value='"+i+"'>" + curDate.format("dddd") + "</button><br>");
			$("#output").append("<textarea id='date-"+i+"' name='date"+i+"' class='day-info-box'>"+curDate.format("MMMM D, YYYY")+"\r\n\r\nKuhn 100\r\n\r\nKuhn 102\r\n\r\nKuhn 200</textarea><br><br>");
			curDate = startDate.add(1, "days")
		}
	});
	$("#reset").button().click(function() {
		eventReset.dialog("open");
	});
	$("#down").button().click(function() {
		eventDownload.dialog("open");
	});
	
	var eventDownload = $("#download-dialog").dialog({
		modal: true,
		height: 300,
		width: 400,
		autoOpen: false,
		open: function() {
			$("#tv-output-form-dl").html("");
			var i = 1;
			var startDate = moment($("#tv-start").prop('value'));
			var endDate = moment($("#tv-end").prop('value'));
			var numDays = endDate.diff(startDate, "days") + 1;
			var curDate = startDate;			
			$(".day-info-box").each(function() {
				$("#tv-output-form-dl").append("<button type='submit' name='linkGetDL' value='"+i+"' class='linkDL'>" + curDate.format("ddd, MMM D") + "</button><br>").append("<input type='hidden' name='date"+i+"' value='"+$("#date-" + i).html()+"'/>");
				curDate = startDate.add(1, "days")
				i++;
			});
		},
		buttons: {
			"Download All": function() {
				var time = 100;
				$(".linkDL").each(function() {
					var dl = this;
					setTimeout(function() {  
						dl.click(); 
					}, time);	
					time += 900;
				});
			},
			Close: function() {
				$(this).dialog("close");
			}
		}
	});
	var eventReset = $("#reset-dialog").dialog({
		modal: true,
		autoOpen: false,
		height: 230,
		width: 400,	
		buttons: {
			"Reset": function() {
				location.reload();
			},
			Cancel: function() {
				$(this).dialog("close");
			}
		}		
	});
});