document.addEventListener("DOMContentLoaded", function() {
    let selectedProtein = [];
    let selectedRice = [];
    let selectedLeaf = [];
    let selectedCheese = [];
    let selectedToppings = [];
    let selectedDressing = [];
    document.getElementById('start').addEventListener('click', function() {
        document.getElementById('frontpage').style.display = 'none';
        document.getElementById('protein').style.display = 'block';
        
    });

    const proteinRadios = document.querySelectorAll('#protein input[type="radio"]');
        proteinRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.checked) {
                    selectedProtein.push(this.value);
                } else {
                    const index = selectedProtein.indexOf(this.value);
                    if (index > -1) {
                        selectedProtein.splice(index, 1);
                    }
                }
            });
        });

    const riceRadios = document.querySelectorAll('#rice input[type="radio"]');
        riceRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.checked) {
                    selectedRice.push(this.value);
                } else {
                    const index = selectedRice.indexOf(this.value);
                    if (index > -1) {
                        selectedRice.splice(index, 1);
                    }
                }
            });
        });
    
    const leafRadios = document.querySelectorAll('#leaf input[type="radio"]');
        leafRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.checked) {
                    selectedLeaf.push(this.value);
                } else {
                    const index = selectedLeaf.indexOf(this.value);
                    if (index > -1) {
                        selectedLeaf.splice(index, 1);
                    }
                }
            });
        });

    const cheeseRadios = document.querySelectorAll('#cheese input[type="radio"]');
        cheeseRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.checked) {
                    selectedCheese.push(this.value);
                } else {
                    const index = selectedCheese.indexOf(this.value);
                    if (index > -1) {
                        selectedCheese.splice(index, 1);
                    }
                }
            });
        });

    /*const riceRadios = document.querySelectorAll('#rice input[type="radio"]');
        riceRadios.forEach(radio => {
            radio.addEventListener('change', function() {
            console.log(`Selected rice: ${selectedRice}`);
        });
    });*/
        
    const toppingsCheckboxes = document.querySelectorAll('#toppings input[type="checkbox"]');
        toppingsCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                if (this.checked) {
                    selectedToppings.push(this.value);
                } else {
                    const index = selectedToppings.indexOf(this.value);
                    if (index > -1) {
                        selectedToppings.splice(index, 1);
                    }
                }
            console.log(`Toppings: ${selectedToppings.join(', ')}`);
            });
        });



    const dressingRadios = document.querySelectorAll('#dressing input[type="radio"]');
        dressingRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.checked) {
                    selectedDressing.push(this.value);
                } else {
                    const index = selectedDressing.indexOf(this.value);
                    if (index > -1) {
                        selectedDressing.splice(index, 1);
                    }
                }
            });
        });


    document.getElementById('next1').addEventListener('click', function() {
        document.getElementById('protein').style.display = 'none';
        document.getElementById('rice').style.display = 'block';
    });
    document.getElementById('next2').addEventListener('click', function() {
        document.getElementById('rice').style.display = 'none';
        document.getElementById('leaf').style.display = 'block';
    });
    document.getElementById('next3').addEventListener('click', function() {
        document.getElementById('leaf').style.display = 'none';
        document.getElementById('cheese').style.display = 'block';
    });
    document.getElementById('next4').addEventListener('click', function() {
        document.getElementById('cheese').style.display = 'none';
        document.getElementById('toppings').style.display = 'block';
    });
    document.getElementById('next5').addEventListener('click', function() {
        document.getElementById('toppings').style.display = 'none';
        document.getElementById('dressing').style.display = 'block';
    });
    document.getElementById('next6').addEventListener('click', function() {
        document.getElementById('dressing').style.display = 'none';

    });


    document.getElementById('back1').addEventListener('click', function() {
        document.getElementById('frontpage').style.display = 'block';
        document.getElementById('protein').style.display = 'none';
        document.getElementById('rice').style.display = 'none';
    });

    document.getElementById('back2').addEventListener('click', function() {
            document.getElementById('protein').style.display = 'block';
            document.getElementById('rice').style.display = 'none';
            document.getElementById('leaf').style.display = 'none';
    });

    document.getElementById('back3').addEventListener('click', function() {
            document.getElementById('rice').style.display = 'block';
            document.getElementById('leaf').style.display = 'none';
            document.getElementById('cheese').style.display = 'none';
    });

    document.getElementById('back4').addEventListener('click', function() {
            document.getElementById('leaf').style.display = 'block';
            document.getElementById('cheese').style.display = 'none';
            document.getElementById('toppings').style.display = 'none';
    });

    document.getElementById('back5').addEventListener('click', function() {
            document.getElementById('cheese').style.display = 'block';
            document.getElementById('toppings').style.display = 'none';
            document.getElementById('dressing').style.display = 'none';

    });

    document.getElementById('back6').addEventListener('click', function() {
            document.getElementById('dressing').style.display = 'block';
            document.getElementById('toppings').style.display = 'none';

    });
});