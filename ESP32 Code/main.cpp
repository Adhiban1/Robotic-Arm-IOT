#include <WiFi.h>
#include <Arduino.h>
#include <ESP32Servo.h>

Servo base, shoulder, elbow, wrist_r, wrist_ud, gripper;

const char *ssid = "ESP32 Access Point";
const char *password = "123456789";

WiFiServer server(80);
void setup()
{
    base.attach(13);
    shoulder.attach(12);
    elbow.attach(14);
    wrist_r.attach(27);
    wrist_ud.attach(26);
    gripper.attach(25);
    Serial.begin(9600);
    pinMode(2, OUTPUT);

    Serial.begin(9600);

    delay(1000);

    WiFi.softAP(ssid, password);
    IPAddress IP = WiFi.softAPIP();
    Serial.print("AP IP address: ");
    Serial.println(IP);
    server.begin();
}

int baseAngle, shoulderAngle, elbowAngle, wristRAngle, wristUAngle, gripperAngle;

void loop()
{

    WiFiClient client = server.available();

    if (client)
    {

        while (client.connected())
        {
            while (client.available() > 0)
            {

                String s = client.readString();
                baseAngle = s.substring(0, 3).toInt();
                shoulderAngle = s.substring(3, 6).toInt();
                elbowAngle = s.substring(6, 9).toInt();
                wristRAngle = s.substring(9, 12).toInt();
                wristUAngle = s.substring(12, 15).toInt();
                gripperAngle = s.substring(15, 18).toInt();
                digitalWrite(2, HIGH);
                base.write(baseAngle);
                delay(100);
                shoulder.write(shoulderAngle);
                delay(100);
                elbow.write(elbowAngle);
                delay(100);
                wrist_r.write(wristRAngle);
                delay(100);
                wrist_ud.write(wristUAngle);
                delay(100);
                gripper.write(gripperAngle);
                delay(1000);
                digitalWrite(2, LOW);
            }
            delay(10);
        }

        client.stop();
        Serial.println("Client disconnected");
    }
}