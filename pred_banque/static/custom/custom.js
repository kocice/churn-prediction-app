
function readURL(input) {
    if (input.files && input.files[0]) {
        var filetype = input.files[0].type;
        // alert(file)
        extensions = ["application/vnd.ms-excel", "text/plain", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]
        if(extensions.includes(filetype)) {
            var reader = new FileReader();

            reader.onload = function(e) {
                $('.image-upload-wrap').hide();

                $('.file-upload-image').attr('src', e.target.result);
                $('.file-upload-content').show();

                $('.image-title').html(input.files[0].name);
            };

            reader.readAsDataURL(input.files[0]);
        }
        else {
            alert('Type de fichier incorrecte');
        }

    } else {
        removeUpload();
    }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
}

$('.image-upload-wrap').bind('dragover', function () {
    $('.image-upload-wrap').addClass('image-dropping');
});

$('.image-upload-wrap').bind('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
});


var Data
var Cells
var getOptions
var click = true;

$(function () {
$("#file").bind("change", function () {
// debugger;
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;//regex for Checking valid files csv of txt

        if (regex.test($("#file").val().toLowerCase())) {
            if (typeof (FileReader) != "undefined") {
                var reader = new FileReader();
                reader.onload = function (e) {
                    var rows = e.target.result.split("\r\n");

                    if(rows.length>0){
                        var first_Row_Cells = splitCSVtoCells(rows[0], ","); //Taking Headings
                        Cells = first_Row_Cells
                        // console.log(Cells);


                        var jsonArray = new Array();
                        for(var i=1;i<(rows.length-1);i++)
                        {
                            var cells = splitCSVtoCells(rows[i], ",");


                            var obj = {};
                            for(var j=0;j<cells.length;j++)
                            {
                                obj[first_Row_Cells[j]] = cells[j];
                            }
                            jsonArray.push(obj);
                        }
                        //Converting to json and json string to div
                        // $("#DivJson").html(JSON.stringify(jsonArray));
                        Data = JSON.stringify(jsonArray)
                        Data = JSON.parse(Data)
                        // console.log(Data)
                        affiche()

                    }
                }
                reader.readAsText($("#file")[0].files[0]);
            }
			else {
                alert("This browser does not support HTML5.");
            }
        } else {
            alert("Select a valid CSV File.");
        }
    });
});
    function splitCSVtoCells(row, separator) {
    return row.split(separator);
}


function affiche() {

    var columnDefs = [];

    Cells.forEach(function(column) {
        columnDefs.push({ field: column },);
        // console.log({ field: column },)
    });
    // console.log(columnDefs)

    // specify the data
    var rowData = Data
    // console.log(Data)


    // let the grid know which columns and what data to use
    const gridOptions = {
        columnDefs: columnDefs,
        rowData: rowData,

        defaultColDef: {
        editable: true,
        // sortable: true,
        flex: 1,
        minWidth: 100,
        // filter: true,
        // resizable: true,
        tooltipComponent: 'customTooltip',
        },
        rowSelection: 'multiple',
        rowMultiSelectWithClick: true,
        rowDragManaged: true,
        headerHeight: 40,
        enableCharts: true,
        pagination : true,
    };

    getOptions = gridOptions


    // setup the grid after the page has finished loading
    // document.addEventListener('DOMContentLoaded', () => {
    //     $("#card").toggle(10000);
        $("#card").toggle(2000)
        const gridDiv = document.querySelector('#myGrid');
        new agGrid.Grid(gridDiv, gridOptions);
        $("#envoyer").removeAttr('hidden');

        // var eGridDiv = document.querySelector('#myGrid');
        // new Grid(eGridDiv, this.gridOptions);
    // });
}

function getSelectedRowData() {
    let selectedNodes = getOptions.api.getSelectedNodes();
	let selectedData = selectedNodes.map(node => node.data);
	// alert(`Selected Nodes:\n${JSON.stringify(selectedData)}`);
    return JSON.stringify(selectedData)
}

$("#envoyer").on("click", function() {
    let dataset = getSelectedRowData();
    $.ajax({
        method: 'POST',
        url: '/affiche_data/',
        data: {
            dataset: dataset,
            // csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },
    })
    .done(function (response) {
        console.log((response))
        $("#myGrid").empty();

        var columnDefs = [];
        for (let key in response[0]) {
            console.log(key);
            columnDefs.push({ field: key },);
        }

        const gridOptions = {
            columnDefs: columnDefs,
            rowData: response,

            defaultColDef: {
                flex: 1,
                minWidth: 100,
                tooltipComponent: 'customTooltip',
            },
            rowDragManaged: true,
            headerHeight: 40,
            enableCharts: true,
            pagination : true,
        };
        click = false;
        $("#envoyer").attr("id","tel")
        $("#tel").html("Télécharger").on("click", function() {
            onBtnExport()
        });
        const gridDiv = document.querySelector('#myGrid');
        new agGrid.Grid(gridDiv, gridOptions);

        function onBtnExport() {
            gridOptions.api.exportDataAsCsv();
        }
    })
})
