function updateData() {
	parcelSelected=$('#parcelSelect').val();
	$('#parcelImage').attr('src', `static/${parcelSelected}_main_pic.jpeg`);
	$.ajax({
		url: 'http://localhost:5000/parcel/' + parcelSelected,
	}).done(function(data){
		$('#data').html(getHtml(data));
	});
}

function loadMap(latitude, longitude) {
	const apiKey = 'AIzaSyCpyssflbjDHDFQGHFZarZ7uRP_QJOM1CQ';
	let mapUrl = `https://www.google.com/maps/embed/v1/place?key=${apiKey}&q=${latitude},${longitude}`;
	map_frame=`<iframe width="500" height="375" frameborder="0" style="border:0" src="${mapUrl}" allowfullscreen></iframe>`;
	$('#map').html(map_frame);
}

function getHtml(responseJson) {
	let html = '';
	let latitude=0;
	let longitude=0;
	const responseObj = JSON.parse(responseJson);

	responseObj.lbstream.parcelid.source.forEach(function(source) {
        name = source.sourcename;
        record = source.record;
        html += '<div class="row source">';
        html += `<h3>Source "${name}"</h3>`;
        html += '</div>';

        if(record) {
                html += '<div class="row">';
                html += '<div class="col header">Name</div>';
                html += '<div class="col header">Description</div>';
                html += '<div class="col header">Value</div>';
                html += '<div class="col-sm header">Update Date</div>';
                html += '<div class="w-100"></div>';
                for(const [key,value] of Object.entries(record)){
                        html += `<div class="col">${key}</div>`;
                        html += `<div class="col">${value.description ? value.description : ''}</div>`;
                        html += `<div class="col">${value.value ? value.value : ''}</div>`;
                        html += `<div class="col-sm">${value.update_date}</div>`;
                        html += '<div class="w-100"></div>';
                        if(key === 'LATITUDE') {
                                latitude = value.value;
                        }
                        if(key === 'LONGITUDE') {
                                longitude = value.value;
                        }
                } 
                html += '</div>';
        }
	});
	loadMap(latitude, longitude);
	return html;
}

$.ready(updateData());

$('#parcelSelect').change(function(){
	updateData();
});