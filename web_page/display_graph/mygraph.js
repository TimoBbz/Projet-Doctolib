    var myContext = document.getElementById("myChart");
    var myChart = new Chart(myContext, {
      type: 'bar',
      data: {
        labels: ["Féminin", "Masculin", "Animaux"],
        datasets: [
           {
           label: "Tous les voyageurs",
           data: [227, 0, 0]
           },{
           label: "1ère Classe",
           data: [107, 115, 2]
           },{
           label: "2ème Classe",
           data: [120, 116, 9]
           }
        ]
      }
    }
  )
