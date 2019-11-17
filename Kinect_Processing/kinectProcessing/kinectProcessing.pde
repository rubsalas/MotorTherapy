/* DESCRIPCIÓN DE ABREVIATURAS:
HL = Hand Left        HR = Hand Right
FL = Feet Left        FR = Feet Right */

import org.openkinect.processing.*;
import processing.net.*;

Server myServer;
Kinect kinect;

float minThresh = 840;
float maxThresh = 890;
int middleX = 320;
int middleY = 240;

int testX = 320;
int testY = 240;

PImage img;
int cont = 0;
String inString ="";

void setup() {
  size(640, 480);
  kinect = new Kinect(this);
  kinect.initDepth();  
  kinect.enableMirror(true);
  img = createImage(kinect.width, kinect.height, RGB);
  myServer = new Server(this, 5204, "192.168.100.80");
  println(Server.ip());
}

void draw(){
  background(0);
  img.loadPixels();
  PImage dImg = kinect.getDepthImage();  
  int[] depth = kinect.getRawDepth();
  
  //Variables para calcular los puntos medios en manos y pies
  float HL_sumX = 0;
  float HL_sumY = 0;
  float HL_totalPixels = 0;

  float HR_sumX = 0;
  float HR_sumY = 0;
  float HR_totalPixels = 0;
  
  float FL_sumX = 0;
  float FL_sumY = 0;
  float FL_totalPixels = 0;
  
  float FR_sumX = 0;
  float FR_sumY = 0;
  float FR_totalPixels = 0;

  float body_sumX = 0;
  float body_sumY = 0;
  float body_totalPixels = 0;

  for(int x=0; x<kinect.width; x++){
    for(int y=0; y<kinect.height; y++){
      int offset = x + y * kinect.width;
      int d = depth[offset];
      
      if(d>minThresh && d<maxThresh){
        img.pixels[offset] = color(255, 0, 150);
        if (x<testX && y<testY){
          //MANO IZQUIERDA
          HL_sumX += x;
          HL_sumY += y;
          HL_totalPixels ++;
        }else if(x>testX && y<testY){
          //MANO DERECHA
          HR_sumX += x;
          HR_sumY += y;
          HR_totalPixels ++;
        }else if(x<testX && y>testY){
          //PIE IZQUIERDO
          FL_sumX += x;
          FL_sumY += y;
          FL_totalPixels ++;
        }else if(x>testX && y>testY){
          //PIE DERECHO
          FR_sumX += x;
          FR_sumY += y;
          FR_totalPixels ++;
        }
      }else if(d>900 && d<925 && y<400 && y>30){
        /* CAMBIAR EL PUNTO MEDIO DEL CUERPO */
        //Calcular el punto medio del cuerpo
        img.pixels[offset] = color(100, 100, 150);
        body_sumX += x;
        body_sumY += y;
        body_totalPixels ++;
      }else{
        img.pixels[offset] = dImg.pixels[offset];
      }
    }
  }
  img.updatePixels();
  image(img, 0, 0);
  
  //Calculo en x y y de los puntos centrales de manos y pies
  float HL_avgX = HL_sumX/HL_totalPixels;
  float HL_avgY = HL_sumY/HL_totalPixels;
  
  float HR_avgX = HR_sumX/HR_totalPixels;
  float HR_avgY = HR_sumY/HR_totalPixels;
  
  float FL_avgX = FL_sumX/FL_totalPixels;
  float FL_avgY = FL_sumY/FL_totalPixels;
  
  float FR_avgX = FR_sumX/FR_totalPixels;
  float FR_avgY = FR_sumY/FR_totalPixels;

  float body_avgX = body_sumX/body_totalPixels;
  float body_avgY = body_sumY/body_totalPixels;
  
  testX = int(body_avgX);
  testY = int(body_avgY) + 100;
  
  //Puntos centrales en manos y pies
  ellipse(HL_avgX, HL_avgY, 15, 15);
  ellipse(HR_avgX, HR_avgY, 15, 15);
  ellipse(FL_avgX, FL_avgY, 15, 15);
  ellipse(FR_avgX, FR_avgY, 15, 15);
  ellipse(body_avgX, body_avgY, 15, 15); 
  
  Client thisClient = myServer.available();
  if (thisClient != null){
    String whatClientSaid = thisClient.readString();
    
    if (whatClientSaid != null){
        whatClientSaid = whatClientSaid.trim();
        println(thisClient.ip() + "t" + whatClientSaid);
    }
  }
 
  if (cont>4){
    myServer.write(int(body_avgX) + "," + int(body_avgY) + "," 
    + int(HL_avgX) + "," + int(HL_avgY) + "," 
    + int(HR_avgX) + "," + int(HR_avgY) + "," 
    + int(FL_avgX) + "," + int(FL_avgY) + "," 
    + int(FR_avgX) + "," + int(FR_avgY));
    cont=0;
  }
  
  cont++;
}
