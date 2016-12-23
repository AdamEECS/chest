def topics_from_url(child='', parent='19776749'):
    query = 'child={}&parent={}'.format(child, parent)
    url_query = '{}?{}'.format(url, query)
    page = requests.post(url_query, data=data, headers=headers)
    dict = page.json()

    for i in dict['msg'][1]:
        if i[0][0] == 'topic':
            t = Topic(topic_id=i[0][2], topic=i[0][1], fid=dict['msg'][0][2])
            print(t)
            t.safe_save()

        if i[0][0] == 'load':
            topics_from_url(child=i[0][2], parent=dict['msg'][0][2])

        if len(i[1]) > 0:
            topics_from_url(parent=i[1][0][0][3])
    return None


def main():
    topics_from_url()


if __name__ == '__main__':
    configure_app()
    # db_manager()
    main()
