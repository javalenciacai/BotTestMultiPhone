class Locators:

    # Localizadores de pagina de inicio "LoginPage"
    txt_user = "//android.widget.EditText[contains(@text, 'Email')]"
    txt_password = "//android.widget.EditText[contains(@text, 'Contraseña')]"
    btn_login = "//android.widget.TextView[contains(@text, 'INGRESAR')]"
    lbl_username_incorrect = "//android.widget.TextView[contains(@text, 'El correo no es válido o puede ser que aún " \
                             "no tienes Siigo nube.')] "
    lbl_password_incorrect = "//android.widget.TextView[contains(@text, 'La contraseña no es válida, confirma la " \
                             "contraseña')] "

    # Localizadores de "HomePage"
    btn_new_element = "//android.widget.TextView[contains(@text, '')]"
    logo = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android" \
           ".widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android" \
           ".view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view" \
           ".ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[" \
           "2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView "
