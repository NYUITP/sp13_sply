from bottle import route, run
import schemaBottle
import listpage


@route('/test1/<url:path>')
# @route('/test2/<weburl:path>,<imgurl:path>')
# @route('/tests')
def test1(url):
    # return schema.helloworld()
    return schemaBottle.schema(url)


# def test2(weburl, imgurl):
#     return listpage.xpath(weburl, imgurl)

run(host='localhost', port=8082, debug=True)
