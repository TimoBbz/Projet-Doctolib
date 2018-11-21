    var myContext = document.getElementById("myChart");
    var myChart = new Chart(myContext, {
      type: 'bar',
      data: {
        labels: ["Qualité des tests", "Absence de plagiat", "Qualité de la syntaxe"],
        datasets: [
           {
           label: "Candidat 1",
           data: [6, 4, 3],
           backgroundColor: 'rgba(255, 99, 132, 0.2)'
           },{
           label: "Candidat 2",
           data: [1,2,5],
           backgroundColor: 'rgba(54, 162, 235, 0.2)'
           },{
           label: "Candidat 3",
           data: [4,0,2],
           backgroundColor: 'rgba(255, 206, 86, 0.2)'
           }
        ],
      },
      options:{title:{
         display:true,
         text:"Résultats des candidats"
      }
    }
  }
)
