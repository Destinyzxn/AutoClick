import win32gui
import win32api
import win32con
import time

while win32gui.FindWindow("MAXScriptDialog", "Batch Animcraft Exporter") != 0:
    time.sleep(0.5)
    cc = {"Frame Rate Change": (188, 263), "帧速率更改": (188, 255)}
    for key in cc:
        while win32gui.FindWindow(None, key) != 0:
            try:
                maxdialog = win32gui.FindWindow(None, key)
                left, top, right, bottom = win32gui.GetWindowRect(maxdialog)
                if maxdialog != 0:
                    val = cc.get(key)
                    win32gui.SetForegroundWindow(maxdialog)
                    win32api.SetCursorPos([left + val[0], top + val[1]])
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.5)
                    win32gui.SetForegroundWindow(maxdialog)
                    win32api.SetCursorPos([left + val[0], top + val[1]])
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            except:
                pass
    else:
        print("Don't need to confirm")
else:
    print("NO Run Batch Animcraft Exporter")