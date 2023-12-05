$(document).ready(function() {
    // Function to populate room categories based on the selected guest house

    function populateRoomCategories() {
        var guesthouse_id = $('#guesthouse').val();
        if (guesthouse_id) {
            $.ajax({
                url: '/get-room-categories/' + guesthouse_id + '/',
                type: 'GET',
                dataType: 'json',
                success: function(data) {
                    $('#room_category').empty();
                    $('#room_category').append($('<option>', {
                        value: '',
                        text: 'Select a room category'
                    }));
                    $.each(data.options, function(index, option) {
                        $('#room_category').append($('<option>', {
                            value: option.id,
                            text: option.room_cat
                        }));
                    });
                }
            });
        } else {
            $('#room_category').empty();
            $('#room_category').append($('<option>', {
                value: '',
                text: 'Select a room category'
            }));
        }
    }
    // Function to populate guest categories based on the selected room category
    function populateGuestCategories() {
        var room_category_id = $('#room_category').val();
        if (room_category_id) {
            $.ajax({
                url: '/get-guest-categories/' + room_category_id + '/',
                type: 'GET',
                dataType: 'json',
                success: function(data) {
                    $('#guest_category').empty();
                    $('#guest_category').append($('<option>', {
                        value: '',
                        text: 'Select a guest category'
                    }));
                    $.each(data.options, function(index, option) {
                        $('#guest_category').append($('<option>', {
                            value: option.id,
                            text: option.guestcategory_name
                        }));
                    });
                }
            });
        } else {
            $('#guest_category').empty();
            $('#guest_category').append($('<option>', {
                value: '',
                text: 'Select a guest category'
            }));
        }
    }
    // Event handlers for guest house and room category dropdowns
    $('#guesthouse').change(populateRoomCategories);
    $('#room_category').change(populateGuestCategories);
    // Initial population of room categories
    populateRoomCategories();
    // Initial population of guest categories
    populateGuestCategories();
});

