class start_testing:
    # ... (other methods and initialization)

    def setup_test_content(self, datas):
        # ... (other setup code)

        # Labels and corresponding keys for the dictionary
        labels_and_keys = [
            ('Headlamp Assembly', 'testheadlamp'),
            ('Top Light', 'testtoplight'),
            ('Supressure Cap', 'testsupres'),
            ('Horn', 'testhorn'),
            ('Exhaust', 'testexhaust'),
        ]

        for label_text, key in labels_and_keys:
            y_position = 275 + labels_and_keys.index((label_text, key)) * 70
            self.show_status_image(label_text, datas['payload'][key], y_position)

    def show_status_image(self, label_text, status, y_position):
        img_path = self.get_image_path(status)
        img_status = self.resize_image(img_path, 30, 30)

        label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='black')
        label.place(x=120, y=y_position)

        status_label = tk.Label(self.frame, image=img_status, bg='black')
        status_label.image = img_status
        status_label.place(x=450, y=y_position)

    def get_image_path(self, status):
        image_dict = {
            'pass': 'right.png',
            'fail': 'cross.png',
            'none': 'blnkbox.png',
        }
        return image_dict.get(status, 'blnkbox.png')
