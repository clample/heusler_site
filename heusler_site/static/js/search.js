//To-Do
		//Get clicked-button to disappear faster!
		
		
		
		//render the information from django server
		var data_from_django = (("{{js_data}}").replace(/&(l|g|quo)t;/g, function(a,b){
			return {
				l : '<',
				g : '>',
				quo: '"'
			}[b];
		}));
		var data_from_django = data_from_django.replace("{{","{");
		var data_from_django = data_from_django.replace("}}","}");
		
		console.log(data_from_django)
		var data_from_django = JSON.parse(data_from_django);
		
		console.log(data_from_django)
		console.log(data_from_django[0])
		
		var mytable = "<table><tbody>";
		for(var i=0; i < data_from_django.length; i++) {
			writeCompound(data_from_django[i])
		}
		
		
		function writeCompound(compoundObject) {
			//writes a compound to the page
			document.getElementById('searchTable').innerHTML += '<tr><td><a href="/heuslers/material/'+ compoundObject.ident + '">'+ compoundObject.name + '</a></tr></td>'; 
		}
		
		
		function clearCompounds() {
			//removes all compounds from the page
			var myNode = document.getElementById('searchTable');
			while (myNode.firstChild) {
				myNode.removeChild(myNode.firstChild);
			}
		}
		
		var clickedButtons = ["","",""]; //stores the compound buttons which are clicked
		
		function compoundSearch(index, element) {
			//index is 0, 1, 2 indicating a search
			//of the A, B, or C atom respectively.
			clearCompounds();
			console.log(clickedButtons)
			
			if (clickedButtons[index] == element) {
				//the button was already clicked so we unclick it
				document.getElementById(index.toString() + clickedButtons[index]).className =
					document.getElementById(index.toString() + clickedButtons[index]).className.replace( /(?:^|\s)clicked-button(?!\S)/g , '' )
				clickedButtons[index] = "";
			} else {
				//a new button was clicked
				if (clickedButtons[index] != "") {
					document.getElementById(index.toString() + clickedButtons[index]).className =
					document.getElementById(index.toString() + clickedButtons[index]).className.replace( /(?:^|\s)clicked-button(?!\S)/g , '' )
				}
				clickedButtons[index] = element;
				document.getElementById(index.toString() + element).className += " clicked-button"
			}
			
			getResults()
		}
		
		function getResults() {
			for(var i=0; i < data_from_django.length; i++) {
				compoundMatches = false;
				
				console.log(clickedStructures)
				
				for(var j=0; j < clickedStructures.length;j++) {
					if (clickedStructures[j] != "") {
						if (data_from_django[i].structure == clickedStructures[j])
							compoundMatches = true;
					}
				}
				if (clickedStructures[0] == "" && clickedStructures[1] == "" && clickedStructures[2] == "") {
					compoundMatches = true;
					
				}
				
				for(var j=0; j < clickedButtons.length; j++) {
					if (clickedButtons[j] != "") {
						switch(j) {
							case 0:
								if (data_from_django[i].Aelement != clickedButtons[j]) {
									compoundMatches = false;
								}
								break;
							case 1:
								if (data_from_django[i].Belement != clickedButtons[j]) {
									compoundMatches = false;
								}
								break;
							case 2:
								if (data_from_django[i].Celement != clickedButtons[j]) {
									compoundMatches = false;
								}
								break;
						}
					}
				}
				
				if (stableClicked && (data_from_django[i].stable == "False")) {
					compoundMatches = false;
				}
				
				if (compoundMatches) {
					writeCompound(data_from_django[i])
				}
			}
		}
		
		var clickedStructures = ["","",""]; //stores the structure buttons which are clicked
		
		function structureSearch(structure) {
			clearCompounds();
			
			if ((structure == "L21") && (clickedStructures[0] == "L21")){
				
				clickedStructures[0] = "";
				document.getElementById("FullHeusler").className =
				document.getElementById("FullHeusler").className.replace( /(?:^|\s)clicked-button(?!\S)/g , '' )
			} else if (structure == "L21" && clickedStructures[0] == "") {
				clickedStructures[0] = "L21";
				document.getElementById("FullHeusler").className += " clicked-button"
			}
			
			if (structure == "C1B" && clickedStructures[1] == "C1B") {
				clickedStructures[1] = "";
				document.getElementById("HalfHeusler").className =
				document.getElementById("HalfHeusler").className.replace( /(?:^|\s)clicked-button(?!\S)/g , '' )
			} else if (structure == "C1B" && clickedStructures[1] == "") {
				clickedStructures[1] = "C1B";
				document.getElementById("HalfHeusler").className += " clicked-button"
			}
			
			if (structure == "Xa" && clickedStructures[2] == "Xa") {
				clickedStructures[2] = "";
				document.getElementById("InverseHeusler").className =
				document.getElementById("InverseHeusler").className.replace( /(?:^|\s)clicked-button(?!\S)/g , '' )
			} else if (structure == "Xa" && clickedStructures[2] == "") {
				clickedStructures[2] = "Xa";
				document.getElementById("InverseHeusler").className += " clicked-button"
			}
			
			
			getResults()
			
		}
		
		var stableClicked = false;
		
		function stableSearch() {
			clearCompounds();
			stableClicked = !stableClicked
			
			if (stableClicked) {
				document.getElementById("stable").className += " clicked-button"
			} else {
				document.getElementById("stable").className =
				document.getElementById("stable").className.replace( /(?:^|\s)clicked-button(?!\S)/g , '' )
			}
			
			getResults()
		
		}
		
		//For the scrollable table
		var $table = $('table.scroll'),
			$bodyCells = $table.find('tbody tr:first').children(),
			colWidth;

		// Adjust the width of thead cells when window resizes
		$(window).resize(function() {
			// Get the tbody columns width array
			colWidth = $bodyCells.map(function() {
				return $(this).width();
			}).get();
			
			// Set the width of thead columns
			$table.find('thead tr').children().each(function(i, v) {
				$(v).width(colWidth[i]);
			});    
		}).resize(); // Trigger resize handler