import sys;

def isValid(acronym,productName):
   
   if not isinstance(acronym,(str, unicode)):
      sys.stderr.write("Usage: acronym parameter must be a string.\n");
      sys.exit(1);
      
   if not isinstance(productName,(str, unicode)):
      sys.stderr.write("Usage: productName parameter must be a string.\n");
      sys.exit(1);
   
   acronym = acronym.upper();
   productName = productName.upper();
      
   word_list  = productName.split(' ');
   word_count = len(word_list);
   
   possib = []
   pcounter = 0;
   for word in word_list:
      possib.append([]);
      for letter in word:
         possib[pcounter].append(letter);
      pcounter += 1;
         
   def quick_recursive(wc,possib,testval,depth,pos,wpos,lastgood):
      
      if depth == 0 and pos == 0:
         boo = False;
         for i in range(wpos,len(possib[depth])):
            if testval[pos] == possib[depth][i]:
               pos += 1;
               boo = True;
               wpos = i + 1;
               lastgood = depth;
               break;

         if boo:
            if pos == len(testval) and wc == depth + 1:
               return True;
               
            elif pos == len(testval):
               return False;
               
            else:
               return quick_recursive(wc,possib,testval,depth,pos,wpos,lastgood);
         
         else:
            return False;

      else:
         if depth + 1 > wc:
            return False;
            
         boo = False;
         
         for i in range(wpos,len(possib[depth])):
            
            if testval[pos] == possib[depth][i]:
               pos += 1;
               boo = True;
               wpos = i + 1;
               
               if lastgood == depth or lastgood == depth -1:
                  lastgood = depth;
                  
               else:
                  return False;
                   
               break;

         if boo:
            if pos == len(testval) and wc == depth + 1:
               return True;
               
            elif pos == len(testval):
               return False;
               
            else:
               chk = quick_recursive(wc,possib,testval,depth,pos,wpos,lastgood);
               
               if chk is False:
                   chk = quick_recursive(wc,possib,testval,depth+1,pos,0,lastgood);
                   
               return chk;
               
         else:
            return quick_recursive(wc,possib,testval,depth+1,pos,0,lastgood);   

            
   chk = quick_recursive(word_count,possib,acronym,0,0,0,-1);    

   if chk:
      return "Valid";
      
   else:
      return "Invalid";

if __name__ == "__main__":
   
   product = "GISi Zombie Tracker 3000";
   print product
   print

   tester = "GIZTK3";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GZT3";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GISEE0";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GZT3k";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GZT";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GZTK";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "BLAH";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   print
   product = "Google Search Engine";
   print product
   print
   
   tester = "GOOSE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GEANIE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "OOSN";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "LEACHE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "OOGLEE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GOOSEEE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GGSEE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GGSE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "SGE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GEANIEOOSN";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "OGGLEE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GGG";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "GGSEA";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   print
   product = "Apple Apple Apple";
   print product
   print
   
   tester = "AAA";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "APAP";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
   tester = "APPLE";   
   print "   " + tester + ": " + isValid(
       acronym     = tester
      ,productName = product 
   );
   
