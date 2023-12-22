# coding: utf-8
#
import uiautomator2 as u2
import time


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    d = u2.connect()

    d(text="My Expenses Debug")
    wait()
    out = d(resourceId="org.totschnig.myexpenses.debug:id/suw_navbar_next").click()
    if not out:
        print("Success: press next")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/suw_navbar_next").click()
    if not out:
        print("Success: press next")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/suw_navbar_done").click()
    if not out:
        print("Success: press start")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/CREATE_COMMAND").click()
    if not out:
        print("Success: press +")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/AmountEditText").click()
    if not out:
        print("Success: press __")
    wait()
    d.click(0.307, 0.776)

    out = d(resourceId="org.totschnig.myexpenses.debug:id/Payee").click()
    if not out:
        print("Success: press __")
    wait()
    d.click(0.328, 0.781)

    out = d(resourceId="org.totschnig.myexpenses.debug:id/CREATE_COMMAND").click()
    if not out:
        print("Success: press √")
    wait()

    out = d(description="更多选项").click()
    if not out:
        print("Success: press ...")
    wait()

    out = d.xpath(
        '//android.widget.ListView/android.widget.LinearLayout[10]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
    if not out:
        print("Success: press >")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[4]').click()
    if not out:
        print("Success: press close")
    wait()

    d.xpath('//*[@resource-id="org.totschnig.myexpenses.debug:id/viewPager"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]').long_click()
