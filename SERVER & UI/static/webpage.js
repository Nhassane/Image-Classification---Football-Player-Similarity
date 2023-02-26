Dropzone.autoDiscover = false;
$(function() {   
    console.log('loaded now')
    $("#try-now-button").click( function() {
        console.log('the try-now button is working')
        document.getElementById("section2").scrollIntoView({behavior: "smooth", block: "center"});
    });
    let dz = new Dropzone("#dropzone", {
        url: "/classify_image",
        maxFiles: 1,
        addRemoveLinks: true,
        dictDefaultMessage: "Some Message",
        autoProcessQueue: false
    })
    dz.on("addedfile", function () {
        console.log('file added')
        if (dz.files[1] !=null) {
            dz.removeFile(dz.files[0]);
        }
    }); 

    dz.on("complete", function() {
        let imageData = dz.files[0].dataURL;
        $.post({
            url: "http://127.0.0.1:5000/classify_image",
            data: { image_data: imageData },
            type: "POST",
            success: function(data, status) {
                console.log(data);
                $(".welcome-msg").hide()
                $(".error").hide()
                response = JSON.parse(data)
                console.log(response[0])
                if (response[0] === undefined) {
                    $("#haaland-result-container").hide()
                    $("#messi-result-container").hide()
                    $("#mahrez-result-container").hide()
                    $("#ronaldo-result-container").hide()
                    $("#mbappe-result-container").hide()
                    $(".similarity").hide()
                    $('.error').show()
                }
                else {
                    player_class = response[0].Player_class_number
                    Similarity = response[0].Similarity
                    if (player_class == 0 ) {
                        $("#haaland-result-container").hide()
                        $("#messi-result-container").hide()
                        $("#mahrez-result-container").hide()
                        $("#ronaldo-result-container").hide()
                        $("#mbappe-result-container").hide()
                        $('.error').hide()
                        $("#haaland-result-container").show()
                        $(".similarity").html("<b>"+Similarity+"</b>")
                    }
                    if (player_class == 1 ) {
                        $("#haaland-result-container").hide()
                        $("#messi-result-container").hide()
                        $("#mahrez-result-container").hide()
                        $("#ronaldo-result-container").hide()
                        $("#mbappe-result-container").hide()
                        $('.error').hide()
                        $("#mahrez-result-container").show()
                        $(".similarity").html("<b>"+Similarity+"</b>")
                    }
                    if (player_class == 2 ) {
                        $("#haaland-result-container").hide()
                        $("#messi-result-container").hide()
                        $("#mahrez-result-container").hide()
                        $("#ronaldo-result-container").hide()
                        $("#mbappe-result-container").hide()
                        $('.error').hide()
                        $("#mbappe-result-container").show()
                        $(".similarity").html("<b>"+Similarity+"</b>")
                    }
                    if (player_class == 3 ) {
                        $("#haaland-result-container").hide()
                        $("#messi-result-container").hide()
                        $("#mahrez-result-container").hide()
                        $("#ronaldo-result-container").hide()
                        $("#mbappe-result-container").hide()
                        $('.error').hide()
                        $("#messi-result-container").show()
                        $(".similarity").html("<b>"+Similarity+"</b>")
                    }
                    if (player_class == 4 ) {
                        $("#haaland-result-container").hide()
                        $("#messi-result-container").hide()
                        $("#mahrez-result-container").hide()
                        $("#ronaldo-result-container").hide()
                        $("#mbappe-result-container").hide()
                        $('.error').hide()
                        $("#ronaldo-result-container").show()
                        $(".similarity").html("<b>"+Similarity+"</b>")
                    }
                }
            }
    });
})
    $("#submitBtn").on('click', function () {
        if (dz.files.length > 0) {
            dz.processQueue();
        }
    })
})