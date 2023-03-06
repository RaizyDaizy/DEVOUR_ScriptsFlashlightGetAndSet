from uniref import WinUniRef

def GetAndSetValue():
    ref = WinUniRef("DEVOUR.exe")
    nolan_beh = ref.find_class_in_image("Assembly-CSharp.dll", "NolanBehaviour")
    initial_flashlight_range = nolan_beh.find_field("initialFlashlightRange")
    addresses = nolan_beh.guess_instance_address()
    for addr in addresses:
        initial_flashlight_range.instance = addr
        initial_flashlight_range.value = 250.0
        print(initial_flashlight_range.value)
if __name__ == "__main__":
    GetAndSetValue()