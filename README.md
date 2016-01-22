# PennApps Expo VIew

Everything is rendered client-side and the site is hosted on GitHub pages, so no backend / scaling issues

### Local setup

1. Clone

2. In that directory, create a webserver, e.g.

  `python -m SimpleHTTPServer`

  If you want to livereload changes, I suggest using [livereload](https://github.com/lepture/python-livereload)

3. See [http://localhost:8000](http://localhost:8000) ( [localhost:35729](http://localhost:35729) if you're using livereload)


### Adding Data

1. Open `data.csv` in **MS Excel or another spreadsheet app**

    There are 5 columns in this sheet:
    - `expo` - Expo number (optional for large hackathons)
    - `table` - Table number
    - `project` - Project Name
    - `sponsors` - Applicable sponsor prizes
    - `link` - Link to project's Devpost page
    - `category` - Optional data field for additional filtering
    - `special`- Additional optional data field

    Paste in submission data & assign table numbers. Otional `category` or `special` columns, can be deleted as necessary or added like:

    ```html
    <table id="expoTable">
      <thead>
        <tr>
          <th class="number">Table</th>
          <th class="name">Project</th>
          <th class="prize">Sponsor Prizes</th>
          <!--<th class="cat">Category</th>-->
        </tr>
      </thead>
      <tbody class="list">
        {{#data}}
          <tr>
            <td class="number">E{{expo}} T{{table}}</td>
            <td class="name"><a href="{{{link}}}" target="_blank">{{project}}</a></td>
            <td class="prize">{{sponsors}}</td>
            <!--<td class="cat">{{category}}</td>-->
          </tr>
        {{/data}}
      </tbody>
    </table>
    ```

3. From DevPost manage/metrics tab, export, _without_ PII.

    Link will be in email. Once you download CSV, open in Excel/copy the the following columns into their matching columns in `data.csv`:

    - `Submission Title` (A) -> `project` (C)
    - `Submission Url` (B) -> `link` (E)
    - `Sponsor Prizes` (usually G or H) -> `sponsors` (D)
    - Repeat for `category` or `special` as needed

4. Assign Expo & table numbers

    FYI: This doesn't assign table numbers.

    **ALSO** You need to the CSV and commit+push to update the list online.


# Filters & sponsors

1. You can use the search box to filter the entire table (all columns) based on any text string

2. You can set the filter by using URL parameters

  Try this, add `?filter=SOME_API_NAME` to url to create a unique, filtered list for each sponsor

  Sent link. App also contains custom print styles that save paper & ink.


### Mobile browsing

Also has mobile styles

