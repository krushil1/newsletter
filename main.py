import smtplib
from email.message import EmailMessage
import requests
import json
import datetime
import os


# Imports all of important credentials from environment
emailAddress = os.environ.get("SECRET_USERNAME")
password = os.environ.get("SECRET_PASSWORD")
usersList = os.environ.get("SECRET_USERSAPI")
dayCycleAPI = os.environ.get("SECRET_DAYCYCLEAPI")
foodAPI = os.environ.get("SECRET_FOODAPI")

now = datetime.datetime.now()  # Gets the current date

EMAIL_ADDRESS = emailAddress  # School Timer's sender email address
EMAIL_PASSWORD = password  # Sender's email password

msg = EmailMessage()
msg['Subject'] = 'School Timer Daily Updates 🐓'  # Subject line for the email
msg['From'] = EMAIL_ADDRESS  # From value for sending the email

# To value for delivering the email to each user
msg['To'] = ""

# API for fetching the day cycle
dayCycle_API = requests.get(dayCycleAPI)
dayCycleData = dayCycle_API.text  # Converts the day cycle API request into text
dayCycleJSON = json.loads(dayCycleData) # Converts the day cycle data into JSON
today = dayCycleJSON['today']  # Gets today's value from JSON
tomorrow = dayCycleJSON['tomorrow']  # Gets tomorrow's value from JSON
dayAfter = dayCycleJSON['nextDay']  # Gets nextDay's value from JSON

breakfastMenuUnfiltered = [] # Creates a list to store all the unfiltered data for breakfast
breakfastMenu = ""  # Stores the filtered breakfast menu inside this

lunchMenuUnfiltered = []  # Creates a list to store all the unfiltered data for lunch
lunchMenu = ""  # Stores the filtered lunch menu inside this

foodMenu_API = requests.get(foodAPI) # Makes request to food menu API
foodMenu = foodMenu_API.text  # Converts the food menu API request into text
foodMenuJSON = json.loads(foodMenu)  # Converts the food menu data into JSON

# Loops through each value inside the breakfast object
for breakfastItem in foodMenuJSON['breakfast']:
    breakfastMenuUnfiltered.append(
        [breakfastItem['product']['name']])  # Gets each breakfast item

# Organizes the breakfast items with commas
breakfastMenu += ', '.join([item[0] for item in breakfastMenuUnfiltered])

# Loops through each value inside the lunch object
for lunchItem in foodMenuJSON['lunch']:
    lunchMenuUnfiltered.append(
        [lunchItem['product']['name']])  # Gets each lunch item

# Organizes the lunch items with commas
lunchMenu += ', '.join([item[0] for item in lunchMenuUnfiltered])


month_name = now.strftime("%b ")  # Gets the month name
day_name = now.strftime("%a ")  # Gets the day name
day_number = now.strftime("%d")  # Gets the day number

# Adds ending the date number
if day_number[0] == '0':
    day_number = day_number[1:]

if day_number[-1] == '1':
    day_number = day_number + 'st'
elif day_number[-1] == '2':
    day_number = day_number + 'nd'
elif day_number[-1] == '3':
    day_number = day_number + 'rd'
else:
    day_number = day_number + 'th'

# Formats the date
date = day_name + month_name + day_number


# Email template that gets sent to the user
msg.set_content('''
<html>
  <table
    width="100%"
    border="0"
    cellspacing="0"
    cellpadding="0"
    bgcolor="#D1D3D3"
    class="mainTable mlBodyBackground"
    dir="ltr"
    background=""
  >
    <tbody>
      <tr>
        <td class="mlTemplateContainer" align="center">
          <!--<![endif]-->

          <!--[if mso 16]>
        <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
          <tr>
            <td bgcolor="#D1D3D3" align="center">
              <!--<![endif]-->

          <!-- Content starts here -->

          <table
            cellpadding="0"
            cellspacing="0"
            border="0"
            align="center"
            width="640"
            style="width: 640px; min-width: 640px"
            class="mobileHide"
          >
            <tbody>
              <tr>
                <td colspan="2" height="20"></td>
              </tr>
              <tr>
                <td
                  align="left"
                  style="
                    color: #111111;
                    font-family: 'Nunito', sans-serif;
                    font-size: 12px;
                    line-height: 150%;
                  "
                ></td>
              </tr>
              <tr>
                <td colspan="2" height="20"></td>
              </tr>
            </tbody>
          </table>

          <table
            align="center"
            cellpadding="0"
            cellspacing="0"
            class="mlContentTable"
            width="640"
            style="
              border-width: 0px;
              border-color: #eaeaea;
              border-style: solid;
              width: 640px;
              min-width: 640px;
            "
          >
            <tbody>
              <tr>
                <td align="center">
                  <table
                    align="center"
                    border="0"
                    bgcolor="#dc3545"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-4"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="40"
                                  class="spacingHeight-40"
                                  style="line-height: 40px; min-height: 40px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            id="transactional-4"
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                  align="left"
                                >
                                  <table
                                    cellspacing="0"
                                    cellpadding="0"
                                    border="0"
                                    align="center"
                                    width="100%"
                                  >
                                    <tbody>
                                      <tr>
                                        <td
                                          align="left"
                                          valign="middle"
                                          width="60"
                                        >
                                          <a
                                            target="_blank"
                                            href="#"
                                            style="
                                              color: #ffffff;
                                              font-family: 'Nunito', sans-serif;
                                              font-size: 12;
                                              line-height: unset;
                                              font-weight: normal;
                                              font-style: normal;
                                              text-decoration: none;
                                            "
                                          >
                                            <img
                                              src="https://i.imgur.com/eCSrCWv.png"
                                              id="logoBlock-4"
                                              border="0"
                                              alt=""
                                              width="60"
                                              style="display: block"
                                            />
                                          </a>
                                        </td>
                                        <td width="20">
                                          <img
                                            src="https://bucket.mlcdn.com/images/default/spacer.gif"
                                            width="1"
                                            height="1"
                                            border="0"
                                            alt=""
                                            style="display: block"
                                          />
                                        </td>
                                        <td align="center" valign="middle">
                                          <table
                                            cellpadding="0"
                                            cellspacing="0"
                                            border="0"
                                            align="center"
                                            width="100%"
                                          >
                                            <tbody>
                                              <tr>
                                                <td align="center">
                                                  <p
                                                    style="
                                                      color: #000000;
                                                      font-family: 'Nunito',
                                                        sans-serif;
                                                      font-size: 12;
                                                      line-height: unset;
                                                      font-weight: normal;
                                                      font-style: normal;
                                                      text-decoration: none;
                                                      text-align: right;
                                                    "
                                                  >
                                                    <span
                                                      style="font-size: 24px"
                                                      ><span
                                                        style="
                                                          color: rgb(
                                                            255,
                                                            255,
                                                            255
                                                          );
                                                        "
                                                        ><span
                                                          style="
                                                            font-size: 24px;
                                                          "
                                                          ><strong
                                                            >Good Morning Pal
                                                            ☀️</strong
                                                          ></span
                                                        ></span
                                                      ></span
                                                    >
                                                  </p>
                                                </td>
                                              </tr>
                                            </tbody>
                                          </table>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="40"
                                  class="spacingHeight-40"
                                  style="line-height: 40px; min-height: 40px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-6"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="60"
                                  class="spacingHeight-60"
                                  style="line-height: 60px; min-height: 60px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="230"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  style="padding: 0px 40px"
                                  align="center"
                                  id="imageBlock-6"
                                >
                                  <a target="_blank" href="#">
                                    <img
                                      src="https://i.imgur.com/qGwz7Zq.png"
                                      border="0"
                                      alt=""
                                      width="230"
                                      style="max-width: 100%; display: block"
                                    />
                                  </a>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="20"
                                  class="spacingHeight-20"
                                  style="line-height: 20px; min-height: 20px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-8"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="30"
                                  class="spacingHeight-30"
                                  style="line-height: 30px; min-height: 30px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td align="center" class="mlContentOuter">
                                  <table
                                    cellpadding="0"
                                    cellspacing="0"
                                    border="0"
                                    align="center"
                                    width="560"
                                    style="
                                      border-top: 1px solid #d1d3d3;
                                      border-collapse: initial;
                                    "
                                    class="mlContentTable"
                                  >
                                    <tbody>
                                      <tr>
                                        <td
                                          height="0"
                                          class="spacingHeight-0"
                                          style="
                                            line-height: 0px;
                                            min-height: 0px;
                                          "
                                        ></td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-10"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="40"
                                  class="spacingHeight-40"
                                  style="line-height: 40px; min-height: 40px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <strong
                                      ><span
                                        style="
                                          line-height: 150%;
                                          color: rgb(233, 74, 53);
                                        "
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgba(187, 34, 85, 0.333);
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(233, 74, 53);
                                            "
                                            ><span
                                              style="
                                                line-height: 150%;
                                                color: rgb(255, 255, 255);
                                              "
                                              >School Timer Daily Update</span
                                            ></span
                                          ></span
                                        ></span
                                      ></strong
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="10"
                                  class="spacingHeight-10"
                                  style="line-height: 10px; min-height: 10px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-13"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <h1
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #293b5f;
                                      font-size: 34px;
                                      line-height: 125%;
                                      font-weight: 400;
                                      margin: 0 0 10px 0;
                                      text-align: center;
                                    "
                                  >
                                    <strong
                                      ><span
                                        style="
                                          line-height: 125%;
                                          color: rgb(87, 87, 87);
                                        "
                                        ><span
                                          style="
                                            line-height: 125%;
                                            color: rgb(255, 255, 255);
                                          "
                                          >{}</span
                                        ></span
                                      ></strong
                                    >
                                  </h1>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-16"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="50"
                                  class="spacingHeight-50"
                                  style="line-height: 50px; min-height: 50px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <span
                                      style="
                                        line-height: 150%;
                                        color: rgb(40, 167, 69);
                                        font-size: 24px;
                                      "
                                      ><strong
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgb(253, 126, 20);
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(255, 209, 69);
                                            "
                                            ><span
                                              style="
                                                line-height: 150%;
                                                color: rgb(234, 236, 237);
                                              "
                                              ><u>Day Cycle</u></span
                                            ></span
                                          ></span
                                        ></strong
                                      ></span
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="20"
                                  class="spacingHeight-20"
                                  style="line-height: 20px; min-height: 20px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-19"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <span
                                      style="
                                        line-height: 150%;
                                        font-size: 28px;
                                        color: rgb(248, 249, 250);
                                      "
                                      ><span
                                        style="
                                          line-height: 150%;
                                          font-size: 24px;
                                          color: rgb(248, 249, 250);
                                        "
                                        >Today</span
                                      ></span
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-22"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <strong
                                      ><span
                                        style="
                                          line-height: 150%;
                                          font-size: 28px;
                                          color: rgb(255, 43, 63);
                                        "
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgb(255, 43, 63);
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(255, 43, 63);
                                            "
                                            ><span
                                              style="
                                                line-height: 150%;
                                                color: rgb(255, 43, 63);
                                              "
                                              >{}</span
                                            ></span
                                          ></span
                                        ></span
                                      ></strong
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="10"
                                  class="spacingHeight-10"
                                  style="line-height: 10px; min-height: 10px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-25"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="10"
                                  class="spacingHeight-10"
                                  style="line-height: 10px; min-height: 10px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <span
                                      style="
                                        line-height: 150%;
                                        font-size: 28px;
                                        color: rgb(87, 87, 87);
                                      "
                                      ><span
                                        style="
                                          line-height: 150%;
                                          font-size: 24px;
                                        "
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgb(87, 87, 87);
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(248, 249, 250);
                                            "
                                            >Tomorrow</span
                                          ></span
                                        ></span
                                      ></span
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-28"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <strong
                                      ><span
                                        style="
                                          line-height: 150%;
                                          font-size: 28px;
                                          color: rgb(255, 43, 63);
                                        "
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgb(255, 43, 63);
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(255, 43, 63);
                                            "
                                            >{}</span
                                          ></span
                                        ></span
                                      ></strong
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-31"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="10"
                                  class="spacingHeight-10"
                                  style="line-height: 10px; min-height: 10px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <span
                                      style="line-height: 150%; font-size: 28px"
                                      ><span
                                        style="
                                          line-height: 150%;
                                          font-size: 24px;
                                        "
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgb(220, 53, 69);
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(87, 87, 87);
                                            "
                                            ><span
                                              style="
                                                line-height: 150%;
                                                color: rgb(248, 249, 250);
                                              "
                                              >Day-after Tomorrow</span
                                            ></span
                                          ></span
                                        ></span
                                      ></span
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-34"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <strong
                                      ><span
                                        style="
                                          line-height: 150%;
                                          font-size: 28px;
                                        "
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgb(201, 59, 59);
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(255, 43, 63);
                                            "
                                            >{}</span
                                          ></span
                                        ></span
                                      ></strong
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="10"
                                  class="spacingHeight-10"
                                  style="line-height: 10px; min-height: 10px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-37"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="50"
                                  class="spacingHeight-50"
                                  style="line-height: 50px; min-height: 50px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <span
                                      style="
                                        line-height: 150%;
                                        color: rgb(40, 167, 69);
                                        font-size: 24px;
                                      "
                                      ><strong
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgb(253, 126, 20);
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(255, 209, 69);
                                            "
                                            ><span
                                              style="
                                                line-height: 150%;
                                                color: rgb(234, 236, 237);
                                              "
                                              ><u>Food Menus</u></span
                                            ></span
                                          ></span
                                        ></strong
                                      ></span
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="20"
                                  class="spacingHeight-20"
                                  style="line-height: 20px; min-height: 20px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-40"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="20"
                                  class="spacingHeight-20"
                                  style="line-height: 20px; min-height: 20px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="200"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  style="padding: 0px 40px"
                                  align="center"
                                  id="imageBlock-40"
                                >
                                  <img
                                    src="https://i.imgur.com/wNTNzpl.png"
                                    border="0"
                                    alt=""
                                    width="200"
                                    style="max-width: 100%; display: block"
                                  />
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="20"
                                  class="spacingHeight-20"
                                  style="line-height: 20px; min-height: 20px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-42"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <strong
                                      ><span
                                        style="
                                          line-height: 150%;
                                          font-size: 24px;
                                        "
                                        ><span
                                          style="
                                            line-height: 150%;
                                            font-size: 24px;
                                          "
                                          ><span
                                            style="
                                              line-height: 150%;
                                              color: rgb(248, 249, 250);
                                            "
                                            >Breakfast</span
                                          ></span
                                        ></span
                                      ></strong
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-45"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="10"
                                  class="spacingHeight-10"
                                  style="line-height: 10px; min-height: 10px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <span
                                      style="
                                        line-height: 150%;
                                        color: rgb(255, 43, 63);
                                      "
                                      ><strong
                                        ><span
                                          style="
                                            line-height: 150%;
                                            font-size: 20px;
                                          "
                                          >{}</span
                                        ></strong
                                      ></span
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="20"
                                  class="spacingHeight-20"
                                  style="line-height: 20px; min-height: 20px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-48"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="20"
                                  class="spacingHeight-20"
                                  style="line-height: 20px; min-height: 20px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <strong
                                      ><span
                                        style="
                                          line-height: 150%;
                                          font-size: 24px;
                                        "
                                        ><span
                                          style="
                                            line-height: 150%;
                                            color: rgb(248, 249, 250);
                                          "
                                          >Lunch</span
                                        ></span
                                      ></strong
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-51"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width=""
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  width=""
                                  style="padding: 0px 40px"
                                  class="mlContentOuter"
                                >
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #1d4450;
                                      font-size: 16px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                      text-align: center;
                                    "
                                  >
                                    <span
                                      style="
                                        line-height: 150%;
                                        color: rgb(255, 43, 63);
                                      "
                                      ><strong
                                        ><span
                                          style="
                                            line-height: 150%;
                                            font-size: 20px;
                                          "
                                          >{}</span
                                        ></strong
                                      ></span
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td
                                  height="50"
                                  class="spacingHeight-50"
                                  style="line-height: 50px; min-height: 50px"
                                ></td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>

                  <table
                    align="center"
                    border="0"
                    bgcolor="#5f5f5f"
                    class="mlContentTable"
                    cellpadding="0"
                    cellspacing="0"
                    width="640"
                    style="width: 640px; min-width: 640px"
                    id="transactional-54"
                  >
                    <tbody>
                      <tr>
                        <td align="center">
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          ></table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            align="center"
                            width="640"
                            style="width: 640px; min-width: 640px"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td align="center" class="">
                                  <table
                                    cellpadding="0"
                                    cellspacing="0"
                                    border="0"
                                    align="center"
                                    width="100%"
                                    style="
                                      border-top: 4px solid #ffffff;
                                      border-collapse: initial;
                                    "
                                    class=""
                                  >
                                    <tbody>
                                      <tr>
                                        <td
                                          height="0"
                                          class="spacingHeight-0"
                                          style="
                                            line-height: 0px;
                                            min-height: 0px;
                                          "
                                        ></td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>

          <table
            align="center"
            bgcolor="#c93b3b"
            class="mlContentTable"
            cellpadding="0"
            cellspacing="0"
            width="640"
            style="width: 640px; min-width: 640px"
          >
            <tbody>
              <tr>
                <td align="center" class="mlFooterText">
                  <table
                    cellpadding="0"
                    cellspacing="0"
                    border="0"
                    align="center"
                    width="640"
                    style="
                      font-family: 'Nunito', sans-serif;
                      font-size: 13px;
                      line-height: 150%%;
                      color: #fff;
                      width: 640px;
                      min-width: 640px;
                    "
                    class="mlContentTable"
                    id="transactional-55"
                  >
                    <tbody>
                      <tr>
                        <td
                          height="80"
                          class="spacingHeight-80"
                          style="line-height: 80px; min-height: 80px"
                        ></td>
                      </tr>
                      <tr>
                        <td
                          style="padding: 0px 40px"
                          class="mlContentOuter"
                          align="left"
                        >
                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            width="49%"
                            align="left"
                            class="marginBottom mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td align="left">
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #fff;
                                      font-size: 13px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                    "
                                  >
                                    <strong
                                      >You received this email because you
                                      signed up on our website.</strong
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>

                          <table
                            cellpadding="0"
                            cellspacing="0"
                            border="0"
                            width="49%"
                            align="right"
                            class="mlContentTable"
                          >
                            <tbody>
                              <tr>
                                <td align="right">
                                  <a target="_blank" href="#">
                                    <img
                                      src="https://i.imgur.com/eCSrCWv.png"
                                      id="logoBlock-55"
                                      border="0"
                                      alt=""
                                      width="50"
                                      style="display: block"
                                    />
                                  </a>
                                </td>
                              </tr>
                              <tr>
                                <td height="20" class="spacingHeight-20"></td>
                              </tr>
                              <tr>
                                <td align="right">
                                  <p
                                    style="
                                      font-family: 'Nunito', sans-serif;
                                      color: #fff;
                                      font-size: 13px;
                                      line-height: 150%;
                                      margin: 0 0 10px 0;
                                      font-weight: 400;
                                      margin-bottom: 0;
                                    "
                                  >
                                    <span style="color: rgb(127, 140, 141)"
                                      ><span style="color: rgb(255, 255, 255)"
                                        ><strong
                                          >© 2023 School Timer. All rights
                                          reserved.</strong
                                        ></span
                                      ></span
                                    >
                                  </p>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </td>
                      </tr>
                      <tr>
                        <td
                          height="80"
                          class="spacingHeight-80"
                          style="line-height: 80px; min-height: 80px"
                        ></td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>

          <table
            cellpadding="0"
            cellspacing="0"
            border="0"
            align="center"
            width="640"
            style="width: 640px; min-width: 640px"
            class="mlContentTable"
          >
            <tbody>
              <tr>
                <td height="40" class="spacingHeight-20"></td>
              </tr>
            </tbody>
          </table>

          <!-- Content ends here -->

          <!--[if mso 16]>
        </td>
        </tr>
        </table>
        <!--<![endif]-->

          <!--[if !mso]><!-- -->
        </td>
      </tr>
    </tbody>
  </table>
</html>
'''.format(date, today, tomorrow, dayAfter, breakfastMenu, lunchMenu), subtype='html')


# Executes the email sending with the html email template
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
