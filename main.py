import parser
import test


# Test
question="In what city and state did Beyonce grow up?"     
answer="Houston, Texas"



# print(question+"    "+answer)
# print(parser.svo_parser(question,[{'text':answer}]))
# parser.renderParseTree(question)


# test.sampleSummarizer("train") 
#Seismologists can use the arrival times of seismic waves in reverse to image the Earth. seismic waves are able to propagate. seismic waves are 410 and 660 kilometers. seismic discontinuities are 410 and 660 kilometers. seismic discontinuities are 410 and 660 kilometers. seismic discontinuities are 410 and 660 kilometers. seismic discontinuities are 410 and 660 kilometers. seismic discontinuities are 410 and 660 kilometers. seismic discontinuities are 410 and 660 kilometers. seismic discontinuities are 410 and
print(parser.svo("Seismologists can use the arrival times of seismic waves in reverse to image the Earth."))