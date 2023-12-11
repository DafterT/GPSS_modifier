first_container_element = document.querySelector('.first_container');
img_in_first_container_element = first_container_element.querySelector('.img_2');
file_input_text_in_first_container_element = first_container_element.querySelector('.text');
file_input_in_first_container_element = first_container_element.querySelector('.fileinput');

second_container_element = document.querySelector('.second_container');
postfix_text_in_second_container_element = second_container_element.querySelector('.text');
img_in_second_container_element = second_container_element.querySelector('.img_1');

third_container_element = document.querySelector('.third_container');
submit_button = third_container_element.querySelector('.submit_button');

file_input_in_first_container_element.addEventListener('change', (element) => {
    if (file_input_in_first_container_element.files.length > 0) {
        file_input_text_in_first_container_element.value = element.target.files[0].name;
    }
});

download = (data, filename, type_) => {
    var file = new Blob([data], {type: type_});
    if (window.navigator.msSaveOrOpenBlob) // IE10+
        window.navigator.msSaveOrOpenBlob(file, filename);
    else { // Others
        var a = document.createElement("a"),
                url = URL.createObjectURL(file);
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(() => {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);  
        }, 0); 
    }
};

shake_submit_button = () => {
    third_container_element.classList.add("shake");
    setTimeout(() => {
        third_container_element.classList.remove("shake");
}, 500)};

submit_button.addEventListener('click', () => {
    if (file_input_in_first_container_element.files.length > 0 &&
        postfix_text_in_second_container_element.value.length != 0) {
            submit_button.disabled = true;
            const reader = new FileReader();  
            reader.onload = async () => {
                let text_result = await eel.get_text_from_python(reader.result, postfix_text_in_second_container_element.value)();
                download(text_result, 'new_file.gpss', 'text/plain');
                submit_button.disabled = false;
            };
            reader.readAsText(file_input_in_first_container_element.files[0]);
    } else {
        shake_submit_button();
    }
});

// Корректность вводимых данных
const regex = /^[a-zA-Z0-9_]*$/;
let old_value = "";

postfix_text_in_second_container_element.addEventListener('input', () => {
    let new_value = postfix_text_in_second_container_element.value;
    if (regex.test(new_value)) {
        old_value = new_value;
    } else {
        postfix_text_in_second_container_element.value = old_value;
    }
});

// Для добавления элементов в форму
img_in_first_container_element.addEventListener('click', () => {
    file_input_in_first_container_element.click();
});

file_input_text_in_first_container_element.addEventListener('click', () => {
    file_input_in_first_container_element.click();
});

img_in_second_container_element.addEventListener('click', () => {
    postfix_text_in_second_container_element.focus();
});
